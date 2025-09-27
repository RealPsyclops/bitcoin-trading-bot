# Pitfalls & Safeties
• One-way positions: cannot hold long+short same asset; opposite orders offset/flip unless Reduce-Only.
• Reduce-Only errors: compute allowable RO size from current position.
• `expiresAfter` rejections burn 5× rate limit—keep clock sync & modest expiries.
• OI caps: long-tail assets can reject opens; check caps.
• Min notional: $10.
• Prefer WS for real-time; backoff using userRateLimit info.

