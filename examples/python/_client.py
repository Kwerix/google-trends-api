"""Shared helper: run the Kwerix Google Trends Actor and return its rows."""

import os
import sys
from decimal import Decimal

from apify_client import ApifyClient

ACTOR = "kwerix/google-trends-api"


def run(run_input: dict, max_charge_usd: str = "1.00") -> list[dict]:
    token = os.environ.get("APIFY_TOKEN")
    if not token:
        sys.exit("Set APIFY_TOKEN (Apify Console → Settings → API & Integrations).")
    client = ApifyClient(token)
    actor_run = client.actor(ACTOR).call(run_input=run_input, max_total_charge_usd=Decimal(max_charge_usd))
    return list(client.dataset(actor_run["defaultDatasetId"]).iterate_items())
