"""An SEO content calendar from seasonality: which keywords to publish for, and by when.

publishBy = next seasonal peak minus the lead time (45 days by default), so new pages have
time to collect rankings before demand peaks. Writes a CSV sorted by date.

    python seasonal_calendar.py "christmas tree" sunscreen "halloween costume" "tax return" --lead 45
"""

import argparse
import csv
import sys

from _client import run

ap = argparse.ArgumentParser()
ap.add_argument("keywords", nargs="+")
ap.add_argument("--geo", default="US")
ap.add_argument("--lead", type=int, default=45, help="days before the peak to publish")
ap.add_argument("--out", default="seasonal-calendar.csv")
args = ap.parse_args()

rows = run({"keywords": args.keywords, "geo": args.geo, "timeRange": "today 5-y",
            "seasonalityLeadDays": args.lead, "includeRelatedQueries": False})
seasonal = sorted((r for r in rows if (r.get("seasonality") or {}).get("isSeasonal")),
                  key=lambda r: r["seasonality"]["publishBy"])
with open(args.out, "w", newline="") as fh:
    w = csv.writer(fh)
    w.writerow(["keyword", "publish_by", "next_peak", "days_until_peak", "peak_months", "window_open"])
    for r in seasonal:
        s = r["seasonality"]
        w.writerow([r["keyword"], s["publishBy"], s["nextPeakDate"], s["daysUntilPeak"], " ".join(s["peakMonths"]), s["publishWindowOpen"]])
        print(f"{s['publishBy']}  {r['keyword']:28} peak {s['nextPeakDate']}")
skipped = [r["keyword"] for r in rows if r not in seasonal]
if skipped:
    print(f"Not seasonal (no fixed peak): {', '.join(skipped)}", file=sys.stderr)
print(f"Wrote {args.out}")
