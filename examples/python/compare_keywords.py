"""Rank any number of keywords by relative popularity on one 0-100 scale.

Google Trends compares at most 5 terms at a time. With compareKeywords the Actor batches
the list with a shared anchor term and rescales every batch to it.

    python compare_keywords.py retinol sunscreen niacinamide "azelaic acid" ceramides tretinoin --anchor retinol
"""

import argparse

from _client import run

ap = argparse.ArgumentParser()
ap.add_argument("keywords", nargs="+")
ap.add_argument("--anchor", help="term shared by every batch; pick one of medium popularity")
ap.add_argument("--geo", default="US")
args = ap.parse_args()

rows = run({"keywords": args.keywords, "geo": args.geo, "timeRange": "today 12-m",
            "compareKeywords": True, "anchorKeyword": args.anchor or args.keywords[0],
            "includeRelatedQueries": False})
ranked = sorted((r for r in rows if r.get("comparison")), key=lambda r: r["comparison"]["rank"])
for r in ranked:
    c = r["comparison"]
    flag = "  (low precision)" if c["lowPrecision"] else ""
    print(f"#{c['rank']:<3} {r['keyword'][:30]:30} {c['averageOnCommonScale']:>7}{flag}")
