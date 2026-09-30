# Google Trends API — examples

Code examples for the **[Google Trends API & Scraper](https://apify.com/kwerix/google-trends-api)** by Kwerix: get Google Trends data for any list of keywords, or everything trending right now in any country, as clean JSON.

- 📊 Interest over time and by region, rising and **breakout** queries
- ⚖️ **Any number of keywords on one scale** (Google Trends stops at 5; the Actor rescales batches with a shared anchor)
- 🗓️ **Seasonality summary**: peak months, next peak and the date to publish by
- 🔥 **Trending Now**: every search trending in a country, with search volume, increase and related searches
- 🤖 Works from Python, JavaScript, plain HTTP and AI agents (MCP)

No browser, no Google account. Pay per result: **$1.50 per 1,000 keywords** or **$0.50 per 1,000 trends**, no start fee. Apify's free plan ($5 of credit every month) covers about 3,300 keywords.

> Looking for a pytrends alternative? pytrends was archived in April 2025 and Google's official Trends API is still an invite-only alpha. These examples show how to get the same data through the Actor instead.

## Quick start (Python)

1. Create a free Apify account and copy your API token from [Console → Settings → API & Integrations](https://console.apify.com/settings/integrations).
2. Install the client and run an example:

```bash
pip install apify-client
export APIFY_TOKEN=<your token>
python examples/python/keyword_analysis.py sunscreen retinol "vitamin c serum"
```

```python
import os
from decimal import Decimal
from apify_client import ApifyClient

client = ApifyClient(os.environ["APIFY_TOKEN"])
run = client.actor("kwerix/google-trends-api").call(
    run_input={"keywords": ["sunscreen", "retinol"], "geo": "US"},
    max_total_charge_usd=Decimal("0.50"),  # hard cap for this run
)
for row in client.dataset(run["defaultDatasetId"]).iterate_items():
    print(row["keyword"], row["trendSlopePctPerYear"], row["breakoutQueries"][:3])
```

## Examples

| File | What it shows |
|---|---|
| [`examples/python/keyword_analysis.py`](examples/python/keyword_analysis.py) | Trend, year-over-year change, seasonality and breakout queries for a keyword list |
| [`examples/python/compare_keywords.py`](examples/python/compare_keywords.py) | Rank any number of keywords by relative popularity on one scale |
| [`examples/python/seasonal_calendar.py`](examples/python/seasonal_calendar.py) | An SEO content calendar: which keywords to publish for, and by when |
| [`examples/python/trending_now.py`](examples/python/trending_now.py) | What is trending now in one or more countries, filtered by category |
| [`examples/javascript/keyword-analysis.mjs`](examples/javascript/keyword-analysis.mjs) | Keyword analysis from Node.js |
| [`examples/javascript/trending-now.mjs`](examples/javascript/trending-now.mjs) | Trending Now from Node.js |
| [`examples/curl/run-sync.sh`](examples/curl/run-sync.sh) | One HTTP call that runs the Actor and returns the results |
| [`examples/mcp/README.md`](examples/mcp/README.md) | Give Claude, ChatGPT or Cursor the Actor as a tool through the Apify MCP server |
| [`sample-output/`](sample-output) | Real output rows for both modes |

## Output at a glance

Keyword analysis returns one row per keyword ([full sample](sample-output/keyword-analysis.json)):

```json
{
  "keyword": "sunscreen",
  "geo": "US",
  "trendSlopePctPerYear": 21.6,
  "yoyChangePct": 55.9,
  "seasonality": {
    "isSeasonal": true,
    "peakMonths": ["Jun", "May", "Apr"],
    "nextPeakDate": "2027-06-08",
    "publishBy": "2027-04-24"
  },
  "breakoutQueries": ["beauty of joseon", "beauty of joseon sunscreen", "joseon sunscreen"]
}
```

Trending Now returns one row per trend ([full sample](sample-output/trending-now.json)):

```json
{
  "keyword": "wnba playoffs",
  "geo": "US",
  "isActive": true,
  "searchVolumeLabel": "5M+",
  "increasePct": 1000,
  "categories": ["Sports"],
  "relatedQueries": ["aces vs fever", "fever", "wnba", "wnba playoffs bracket"]
}
```

Google Trends values are relative (0–100), not search volumes. Full field reference, input options and FAQ: **[apify.com/kwerix/google-trends-api](https://apify.com/kwerix/google-trends-api)**.

## License

MIT for the examples in this repository. The Actor itself is a paid service on Apify Store. Kwerix is not affiliated with Google; "Google Trends" is a trademark of Google LLC.
