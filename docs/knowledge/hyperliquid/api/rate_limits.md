# Rate Limits
REST: aggregated weights (explorer calls ~40); use S3 for large history.
WS: <=100 connections, <=1000 subs, <=2000 msgs/min across sockets; <=100 inflight post msgs.
User telemetry: info {type: "userRateLimit"} for usage/caps; backoff if near caps.
