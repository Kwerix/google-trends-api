"""Trend, year-over-year change, seasonality and breakout queries for a keyword list.

    python keyword_analysis.py sunscreen retinol "vitamin c serum" --geo US
"""

import argparse

from _client import run

ap = argparse.ArgumentParser()
ap.add_argument("keywords", nargs="+")
ap.add_argument("--geo", default="US", help="country code, empty for worldwide")
args = ap.parse_args()

rows = run({"keywords": args.keywords, "geo": args.geo, "timeRange": "today 5-y"})
pct = lambda v: "-" if v is None else f"{v}%"
print(f"{'keyword':24} {'avg':>5} {'trend/yr':>9} {'YoY':>7}  seasonal  peak months       breakout")
for r in rows:
    s = r.get("seasonality") or {}
    print(f"{r['keyword'][:24]:24} {r['averageInterest'] or 0:>5} {pct(r['trendSlopePctPerYear']):>9} "
          f"{pct(r['yoyChangePct']):>7}  {str(s.get('isSeasonal', '-')):8}  {', '.join(s.get('peakMonths', [])):16} "
          f"{', '.join(r['breakoutQueries'][:2])}")
