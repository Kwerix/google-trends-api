# Use the Google Trends API from AI agents (MCP)

The Apify MCP server can expose this Actor as a tool to Claude, ChatGPT, Cursor and other MCP clients.

## Only this Actor

```
https://mcp.apify.com?tools=kwerix/google-trends-api
```

Most clients accept this shape (check your client's MCP docs for the exact keys):

```json
{
  "mcpServers": {
    "apify": { "type": "http", "url": "https://mcp.apify.com?tools=kwerix/google-trends-api" }
  }
}
```

The first connection opens a browser to sign in to Apify. For clients that only support local servers:

```json
{
  "mcpServers": {
    "apify": {
      "command": "npx",
      "args": ["-y", "@apify/actors-mcp-server@latest", "--tools", "kwerix/google-trends-api"],
      "env": { "APIFY_TOKEN": "<your token>" }
    }
  }
}
```

## Prompts that work well

- "Is 'sunscreen' seasonal in the US, and by when should I publish content for the next peak?"
- "Rank these 20 skincare keywords by Google Trends popularity on one scale."
- "What is trending in Spain right now in Sports and Technology?"
- "Which queries are breaking out around 'ai agents'?"

The Actor's defaults keep results compact (one row per keyword, no raw timeline), so they fit in a model's context. Cost: $0.0015 per keyword, $0.0005 per trend.
