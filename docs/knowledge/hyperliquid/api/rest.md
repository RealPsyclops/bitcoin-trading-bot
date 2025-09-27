# REST

- **Base**: <fill>
- **Auth**: <fill> (HMAC? key/secret? headers?)
- **Endpoints**:
  - `POST /order` — place order
  - `POST /cancel` — cancel order

**Notes**
- Include idempotency keys.
- Log request/response (sans secrets) for reproducibility.
