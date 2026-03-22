# Implement role-based access control for API keys

Added granular permission system for API keys: read-only, read-write, admin scopes. Each key can be scoped to specific endpoints. Includes migration to add `permissions` JSONB column to `api_keys` table.
