# Fees & Funding
Trading fees: tiered by 14D rolling volume; assessed daily UTC. Typical ranges: maker ~0.01%, taker ~0.035% (verify live schedule in app).
Funding: hourly; capped at 4%/hour; use info {type:"fundingHistory"} for realized carry.
PnL = Realized (fills - fees) + Funding - withdrawals/transfer fees.
