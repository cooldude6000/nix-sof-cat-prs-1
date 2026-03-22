# Stream CSV export to avoid memory overflow on large reports

Replaced in-memory CSV generation with streaming response using chunked transfer encoding. Memory usage drops from 2GB to 50MB for 100k-row exports. Added progress tracking via SSE.
