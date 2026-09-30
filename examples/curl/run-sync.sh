#!/usr/bin/env bash
# Run the Actor and get the results in one HTTP call (for runs under 5 minutes).
# maxTotalChargeUsd caps what this run can cost.
#   APIFY_TOKEN=... ./run-sync.sh
set -euo pipefail
curl -s -X POST "https://api.apify.com/v2/acts/kwerix~google-trends-api/run-sync-get-dataset-items?maxTotalChargeUsd=0.5" \
  -H "Authorization: Bearer ${APIFY_TOKEN:?set APIFY_TOKEN}" \
  -H "Content-Type: application/json" \
  -d '{"keywords": ["sunscreen", "retinol"], "geo": "US", "timeRange": "today 5-y"}'
