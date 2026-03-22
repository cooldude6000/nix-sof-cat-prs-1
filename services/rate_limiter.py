# Add rate limiting per API key with configurable thresholds

Implemented token bucket rate limiting per API key using Redis. Default: 100 req/min for standard keys, 1000 req/min for enterprise. Configurable per customer. Returns standard 429 with Retry-After header.
