# Fix dashboard query performance with pagination and indexing

Added database indexes on `created_at` and `customer_id` columns. Implemented cursor-based pagination for the dashboard endpoint to replace OFFSET queries. Reduces p95 latency from 30s to 800ms for accounts with 10k+ records.
