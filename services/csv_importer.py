# Fix data import failing silently on malformed CSV rows

CSV import was catching all exceptions and logging at DEBUG level, making failures invisible. Added row-level validation with detailed error reporting. Failed rows are collected and returned to the user with line numbers and reasons.
