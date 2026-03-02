# -*- coding: utf-8 -*-
"""ticker_universe_kr.py 생성: KOSPI 200 + KOSDAQ 100, marcap 기반"""
import os
import pandas as pd

BASE = os.path.dirname(os.path.abspath(__file__))
MARCAP = os.path.join(BASE, "cache", "marcap-2026.parquet")
META = os.path.join(BASE, "meta_cache_kr.csv")
OUT = os.path.join(BASE, "ticker_universe_kr.py")

def main():
    df = pd.read_parquet(MARCAP)
    latest = df["Date"].max()
    d = df[df["Date"] == latest]
    exc = "ETF|etf|스팩|SPAC|우선주|우$|우B|우A"
    kospi = d[d["Market"] == "KOSPI"].copy()
    kospi = kospi[~kospi["Name"].astype(str).str.contains(exc, na=False, regex=True)]
    kospi = kospi[~kospi["Name"].astype(str).str.endswith("우")]
    kospi = kospi[kospi["Code"].astype(str).str.match(r"^[0-9]{6}$")]
    kospi = kospi.sort_values("Marcap", ascending=False).head(200)
    kosdaq = d[d["Market"] == "KOSDAQ"].copy()
    kosdaq = kosdaq[~kosdaq["Name"].astype(str).str.contains(exc, na=False, regex=True)]
    kosdaq = kosdaq[kosdaq["Code"].astype(str).str.match(r"^[0-9]{6}$")]
    kosdaq = kosdaq.sort_values("Marcap", ascending=False).head(100)

    sector_map = {}
    if os.path.exists(META):
        meta = pd.read_csv(META, encoding="utf-8")
        for _, r in meta.iterrows():
            t = str(r.get("Ticker", "")).strip().upper()
            s = str(r.get("Sector", "Industrials")).strip()
            if t and s:
                sector_map[t] = s

    lines = [
        '# ticker_universe_kr.py',
        '# -----------------------------',
        '# 한국 증시 유니버스 — 코스피 200 + 코스닥 100',
        '# Yahoo Finance: KOSPI=XXXXXX.KS, KOSDAQ=XXXXXX.KQ',
        '# marcap 시총 상위, ETF/우선주 제외',
        '# -----------------------------',
        '',
        '# 코스피 200 (시총 상위)',
        'KOSPI_200 = [',
    ]
    for _, r in kospi.iterrows():
        t = str(r["Code"]).zfill(6) + ".KS"
        n = str(r["Name"]).strip()
        lines.append(f'    "{t}",  # {n}')
    lines.append("]")
    lines.append("")
    lines.append("# 코스닥 100 (시총 상위)")
    lines.append("KOSDAQ_100 = [")
    for _, r in kosdaq.iterrows():
        t = str(r["Code"]).zfill(6) + ".KQ"
        n = str(r["Name"]).strip()
        lines.append(f'    "{t}",  # {n}')
    lines.append("]")
    lines.append("")
    lines.append("# 중복 제거 후 정렬")
    lines.append("TICKERS = sorted(list(dict.fromkeys(t.upper().strip() for t in KOSPI_200 + KOSDAQ_100)))")
    lines.append("")
    lines.append("# 티커 → 회사명")
    lines.append("TICKER_TO_NAME = {")
    name_entries = []
    for _, r in kospi.iterrows():
        t = str(r["Code"]).zfill(6) + ".KS"
        n = str(r["Name"]).strip().replace('"', "'")
        name_entries.append(f'    "{t}": "{n}"')
    for _, r in kosdaq.iterrows():
        t = str(r["Code"]).zfill(6) + ".KQ"
        n = str(r["Name"]).strip().replace('"', "'")
        name_entries.append(f'    "{t}": "{n}"')
    lines.append(",\n".join(name_entries))
    lines.append("}")
    lines.append("")
    lines.append("NAME_TO_TICKER = {v: k for k, v in TICKER_TO_NAME.items()}")
    lines.append("")
    lines.append("# 티커 → 섹터 (meta_cache_kr 기반, 없으면 Industrials)")
    lines.append("TICKER_TO_SECTOR = {")
    sector_entries = []
    for _, r in kospi.iterrows():
        t = str(r["Code"]).zfill(6) + ".KS"
        s = sector_map.get(t, "Industrials")
        sector_entries.append(f'    "{t}": "{s}"')
    for _, r in kosdaq.iterrows():
        t = str(r["Code"]).zfill(6) + ".KQ"
        s = sector_map.get(t, "Industrials")
        sector_entries.append(f'    "{t}": "{s}"')
    lines.append(",\n".join(sector_entries))
    lines.append("}")
    with open(OUT, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))
    print(f"[OK] {OUT} 생성. KOSPI {len(kospi)} + KOSDAQ {len(kosdaq)}")

if __name__ == "__main__":
    main()
