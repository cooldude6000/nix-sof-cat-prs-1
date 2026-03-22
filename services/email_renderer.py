# Fix email template rendering breaking with special characters

HTML entities in customer names and data fields were not being escaped before template rendering. Fixed the Jinja2 template pipeline to auto-escape all dynamic content. Added test suite for edge cases (unicode, HTML injection).
