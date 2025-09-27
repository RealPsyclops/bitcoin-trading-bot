# Take Profit / Stop Loss (TP/SL)
Trigger uses mark price. Market TP/SL ~10% slippage tolerance.
Limit TP/SL: pick aggressive limit to ensure fill in gaps; too tight may rest.
Parent OCO: children placed only if parent fully fills or partial + cancel for insufficient margin. Manual cancel after partial fill cancels children.
Recommendation: for bots, prefer position-level TP/SL for robustness.
