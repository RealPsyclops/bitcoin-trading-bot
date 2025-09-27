# Hyperliquid — SUMMARY

**Purpose**: Give humans a fast, ~1‑page understanding of how we integrate Hyperliquid.

- **What we trade**: Perps on BTC, ETH, + selected alts
- **Execution**: REST for orders; WS for market data + private fills
- **Risk link**: We mirror constraints from `hyperliquid_llm_ref.yaml`

## Key integration notes
- Respect rate limits and exponential backoff (see `api/rate_limits.md`).
- Use POST-only or reduce-only where appropriate to avoid taker creep.
- Kill switch and position caps must be enforced pre-trade.

## Open Items
- Fill in REST/WS base URLs and auth steps.
- Finalize allowed leverage by asset list.
