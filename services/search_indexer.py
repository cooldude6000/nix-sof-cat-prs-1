# Optimize Elasticsearch indexing pipeline for real-time search

Switched from bulk indexing every 5 minutes to near-real-time indexing with 1-second refresh intervals for recent data. Added index aliases for zero-downtime reindexing. Search latency reduced from 5min lag to <2s.
