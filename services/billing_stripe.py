# Migrate billing service from Stripe v2 to v3 API

Upgraded Stripe SDK from v2 to v3. Migrated all payment intents, subscription management, and invoice generation to the new API. Added idempotency keys for all mutating operations. Backward compatible — no customer-facing changes.
