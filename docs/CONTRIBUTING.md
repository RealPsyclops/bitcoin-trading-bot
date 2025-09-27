# Contributing — Knowledge Base & Global Context

**Principle**: Repo is the source of truth. Chats are routers and workrooms.

## Workflow
1. Paste new info into the **Global Context** chat.
2. The router proposes `{files_to_update}` under `docs/knowledge/*`.
3. You PR those edits and run `scripts/verify_kb.py`.

## Component Threads
- Use clear names like `signals/ema_rsi`, `exec/order_translation`, `risk/pnl_limits`.
- Begin each thread with: “Use context from `docs/GLOBAL_CONTEXT.md` and `docs/knowledge/index.json` (Hyperliquid collection).”
