// Trend, seasonality and breakout queries for a keyword list.
//   npm install && APIFY_TOKEN=... node keyword-analysis.mjs sunscreen retinol
import { ApifyClient } from 'apify-client';

const keywords = process.argv.slice(2);
if (!keywords.length) throw new Error('Usage: node keyword-analysis.mjs <keyword> [keyword...]');

const client = new ApifyClient({ token: process.env.APIFY_TOKEN });
const run = await client.actor('kwerix/google-trends-api').call(
    { keywords, geo: 'US', timeRange: 'today 5-y' },
    { maxTotalChargeUsd: 1 },
);
const { items } = await client.dataset(run.defaultDatasetId).listItems();
for (const row of items) {
    const s = row.seasonality ?? {};
    console.log(`${row.keyword}: trend ${row.trendSlopePctPerYear}%/yr, YoY ${row.yoyChangePct}%, `
        + `seasonal ${s.isSeasonal ?? '-'}${s.publishBy ? `, publish by ${s.publishBy}` : ''}, `
        + `breakout: ${row.breakoutQueries.slice(0, 3).join(', ') || '-'}`);
}
