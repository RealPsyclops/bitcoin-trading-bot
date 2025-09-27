# Global Context (GC)

You’re in the repo’s *knowledge hub*. This is the canonical index and usage guide.

## What lives here
- **Hyperliquid**: curated, LLM-ready references, API notes, constraints, examples.
- **Architecture, Risk & Policy**: project-wide rules your code must obey.

## How to reference this from any chat
Paste (or pin) this line in a new chat:
```
Use context from docs/GLOBAL_CONTEXT.md and docs/knowledge/index.json (Hyperliquid collection).
```
Optionally add an include list of specific paths (fast + explicit).

## Day-to-day flow (recommended)
1. **Triage in the Global Context chat** (router role):
   - Paste new info → get a proposed storage path under `docs/knowledge/`.
   - Receive: `{files_to_update}`, `{threads_to_use}`, `{open_questions}`.

2. **Commit to repo** (source of truth):
   - Add/modify files proposed by the router.
   - Run `scripts/verify_kb.py` before committing to catch stale links.

3. **Work in component chats** (clean boundaries):
   - Examples:
     - `exec/order_translation`
     - `data/ingestion_hyperliquid`
     - `risk/pnl_limits`
     - `signals/ema_rsi`
   - Each chat references specific repo paths from this GC.

## Index
- `docs/knowledge/index.json`: machine-readable collections
- `docs/knowledge/hyperliquid/hyperliquid_llm_ref.yaml`: compact spec consumed by LLMs and bot code
- `docs/knowledge/hyperliquid/SUMMARY.md`: human-readable notes and gotchas
- `docs/knowledge/hyperliquid/api/*.md`: short API pages
- `docs/knowledge/hyperliquid/examples/*.json`: tiny, copy-pastable request/response examples

## Guardrails
- Update policy/constraints **here first** → reflect in code.
- Never let code drift from these files.
