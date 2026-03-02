#!/usr/bin/env python
# refresh_meta_kr.py — 한국 증시 메타(시총/섹터) 캐시 최신화
# 실행: python refresh_meta_kr.py
# yfinance 우선, 없으면 pykrx fallback (코스닥 포함)

import os
import sys
from datetime import datetime

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import yfinance as yf
import pandas as pd
import numpy as np
import scanner_config as cfg
from ticker_universe_kr import TICKERS, TICKER_TO_SECTOR

META_CACHE_KR_PATH = os.path.join(os.path.dirname(__file__), "meta_cache_kr.csv")
KRW_PER_USD = getattr(cfg, "KRW_PER_USD", 1464.0)


def _fetch_pykrx_caps():
    """pykrx로 KOSPI/KOSDAQ 전체 시가총액 조회 (fallback용)."""
    caps = {}
    try:
        from pykrx import stock
        dt = datetime.now().strftime("%Y%m%d")
        for market in ("KOSPI", "KOSDAQ"):
            df = stock.get_market_cap(dt, market=market)
            if df is not None and not df.empty and "시가총액" in df.columns:
                for code, row in df.iterrows():
                    val = row.get("시가총액")
                    if pd.notna(val) and np.isfinite(float(val)):
                        caps[str(code).zfill(6)] = float(val)
    except Exception as e:
        print(f"[pykrx] fallback 실패: {e}")
    return caps


def _fetch_fdr_caps():
    """FinanceDataReader로 시가총액 조회 (pykrx 실패 시 fallback)."""
    caps = {}
    try:
        import FinanceDataReader as fdr
        for market in ("KRX-MARCAP", "KRX", "KOSPI", "KOSDAQ"):
            df = fdr.StockListing(market)
            if df is None or df.empty:
                continue
            code_col = "Code" if "Code" in df.columns else "Symbol"
            for col in ("MarCap", "Marcap", "시가총액", "MarketCap"):
                if col in df.columns:
                    for _, row in df.iterrows():
                        code = str(row.get(code_col, "")).zfill(6)
                        val = row.get(col)
                        if code and pd.notna(val) and np.isfinite(float(val)):
                            caps[code] = float(val)
                    break
            if caps:
                break
    except Exception as e:
        print(f"[FinanceDataReader] fallback 실패: {e}")
    return caps


def _fetch_marcap_caps():
    """marcap 데이터셋으로 시가총액 조회 (pykrx/FDR 실패 시 fallback). 코스닥 포함. GitHub에서 다운로드."""
    caps = {}
    try:
        import scanner as sc
        df = sc._load_marcap_latest()
        if df is None or df.empty or "Code" not in df.columns:
            return caps
        for mcol in ("Marcap", "MarCap", "시가총액"):
            if mcol not in df.columns:
                continue
            for _, row in df.iterrows():
                code = str(row.get("Code", "")).zfill(6)
                val = row.get(mcol)
                if code and pd.notna(val) and np.isfinite(float(val)):
                    v = float(val)
                    caps[code] = v * 1_000_000 if v < 1e10 else v
            break
    except Exception as e:
        print(f"[marcap] fallback 실패: {e}")
    return caps


def refresh_meta_kr():
    """모든 KR 티커의 시총(KRW)·섹터를 yfinance에서 조회. 없으면 pykrx fallback."""
    rows = []
    need_pykrx = []
    n = len(TICKERS)
    for i, ticker in enumerate(TICKERS, 1):
        try:
            t = yf.Ticker(ticker)
            info = t.info
            mc = info.get("marketCap")
            curr = str(info.get("currency", "")).upper()
            sector = info.get("sector") or info.get("industry") or TICKER_TO_SECTOR.get(ticker.upper(), "Unknown")

            if mc is not None and np.isfinite(float(mc)):
                mc = float(mc)
                mktcap_krw = mc if curr == "KRW" else mc * KRW_PER_USD
            else:
                mktcap_krw = None
                need_pykrx.append((i, ticker, sector))

            rows.append({
                "Ticker": ticker.upper(),
                "MarketCap_KRW": mktcap_krw,
                "Sector": sector or "Unknown",
            })
            mkt_str = f"MktCap={mktcap_krw/1e8:,.0f}억" if mktcap_krw else "MktCap=None"
            print(f"[{i}/{n}] {ticker}: {mkt_str} Sector={sector}")
        except Exception as e:
            sector = TICKER_TO_SECTOR.get(ticker.upper(), "Unknown")
            rows.append({"Ticker": ticker.upper(), "MarketCap_KRW": None, "Sector": sector})
            need_pykrx.append((i, ticker, sector))
            print(f"[{i}/{n}] {ticker}: ERROR {e} → Sector fallback={sector}")

    if need_pykrx:
        print(f"\n[pykrx] 시가총액 비어있는 {len(need_pykrx)}종목 fallback 조회 중...")
        fallback_caps = _fetch_pykrx_caps()
        src = "pykrx"
        if not fallback_caps:
            print("[FinanceDataReader] pykrx 비어있음 → FDR fallback 시도...")
            fallback_caps = _fetch_fdr_caps()
            src = "FDR"
        if not fallback_caps:
            print("[marcap] FDR 비어있음 → marcap fallback 시도...")
            fallback_caps = _fetch_marcap_caps()
            src = "marcap"
        for idx, (i, ticker, sector) in enumerate(need_pykrx):
            code = ticker.split(".")[0].zfill(6)
            mktcap_krw = fallback_caps.get(code)
            for r in rows:
                if r["Ticker"] == ticker.upper():
                    r["MarketCap_KRW"] = mktcap_krw
                    break
            mkt_str = f"MktCap={mktcap_krw/1e8:,.0f}억" if mktcap_krw else "MktCap=None"
            print(f"  [{i}/{n}] {ticker}: {mkt_str} (fallback:{src})")

    df = pd.DataFrame(rows)
    df.to_csv(META_CACHE_KR_PATH, index=False, encoding="utf-8-sig")
    print(f"\n저장 완료: {META_CACHE_KR_PATH} ({len(df)} 종목)")


if __name__ == "__main__":
    refresh_meta_kr()
