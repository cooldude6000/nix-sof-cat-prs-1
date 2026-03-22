# Fix race condition in real-time notification queue

Added distributed locking via Redis SETNX to prevent duplicate notification processing. Fixed a race condition where two workers could pick up the same notification job, causing users to receive duplicate alerts.
