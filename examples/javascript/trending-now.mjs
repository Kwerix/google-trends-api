// What is trending now in one or more countries.
//   npm install && APIFY_TOKEN=... node trending-now.mjs US GB
import { ApifyClient } from 'apify-client';

const trendingGeos = process.argv.slice(2).length ? process.argv.slice(2) : ['US'];
const client = new ApifyClient({ token: process.env.APIFY_TOKEN });
const run = await client.actor('kwerix/google-trends-api').call(
    { mode: 'trending', trendingGeos, trendingHours: '24', trendingActiveOnly: true },
    { maxTotalChargeUsd: 1 },
);
const { items } = await client.dataset(run.defaultDatasetId).listItems();
items.sort((a, b) => (b.searchVolume ?? 0) - (a.searchVolume ?? 0));
for (const t of items.slice(0, 20)) console.log(`${t.geo} ${t.searchVolumeLabel.padStart(6)}  ${t.keyword}  [${t.categories.join(', ')}]`);
