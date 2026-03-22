# Fix GraphQL N+1 query problem in customer list endpoint

Added DataLoader pattern to batch database queries in the GraphQL resolver. Customer list endpoint was making 1 + N queries (one per customer for related data). Now uses 3 batched queries regardless of list size.
