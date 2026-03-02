# -*- coding: utf-8 -*-
"""
한국 티커 유니버스 갱신: marcap parquet에서 KOSPI 200 + KOSDAQ 100 추출.
- gen_ticker_universe_kr.py 호출
- cache/marcap-*.parquet 필요
"""
import os
import sys

BASE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, BASE)


def refresh():
    try:
        from gen_ticker_universe_kr import main
        main()
        return True
    except Exception as e:
        print(f"[KR] 갱신 실패: {e}")
        return False


if __name__ == "__main__":
    refresh()
