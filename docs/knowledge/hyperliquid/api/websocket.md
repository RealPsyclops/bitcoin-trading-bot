# REST
Base: https://api.hyperliquid.xyz/exchange
Testnet: https://api.hyperliquid-testnet.xyz/exchange
Auth/Signing: Use Python SDK pattern (nonce=ms timestamp; include `expiresAfter` only if needed).
Place order fields: a (asset), b (isBuy), p (px), s (sz), r (reduceOnly),
t.limit.tif: Alo|Ioc|Gtc; t.trigger: { isMarket, triggerPx, tpsl: tp|sl }
Min order notional: $10. Stale `expiresAfter` costs 5× rate limit. 
