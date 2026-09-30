"""What is trending now in one or more countries, biggest first.

    python trending_now.py US GB ES --hours 24 --category Sports --category Technology
"""

import argparse

from _client import run

ap = argparse.ArgumentParser()
ap.add_argument("countries", nargs="+", help="country codes, e.g. US GB ES")
ap.add_argument("--hours", default="24", choices=["4", "24", "48", "168"])
ap.add_argument("--category", action="append", default=[], help="e.g. Sports, Technology, Entertainment")
ap.add_argument("--active-only", action="store_true")
ap.add_argument("--top", type=int, default=10, help="rows to print per country")
args = ap.parse_args()

rows = run({"mode": "trending", "trendingGeos": args.countries, "trendingHours": args.hours,
            "trendingCategories": args.category, "trendingActiveOnly": args.active_only})
for geo in args.countries:
    trends = sorted((r for r in rows if r["geo"] == geo.upper()), key=lambda r: -(r["searchVolume"] or 0))
    print(f"\n{geo.upper()}: {len(trends)} trends")
    for r in trends[: args.top]:
        state = "active" if r["isActive"] else "ended"
        print(f"  {r['searchVolumeLabel']:>6}  {r['keyword'][:40]:40} {state:6} {', '.join(r['categories'])}")
