# Architecture (High-level)

- **API Inputs**: Market data (WS), account/fills (WS private), orders (REST)
- **Indicators/Algos**: Each indicator as an **independent module** (plug-and-play)
- **Mainframe (Execution Engine)**:
  - Input: Price, Trade size (relative to portfolio), Leverage, Trigger, Side (Long/Short)
  - Output: Market/Limit orders; PnL tracking
- **Risk Layer**: Enforce `RISK_POLICY.yaml` and `hyperliquid_llm_ref.yaml`
