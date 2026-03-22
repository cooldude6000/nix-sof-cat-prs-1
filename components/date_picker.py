# Fix date picker not respecting user locale settings

The date picker component was hardcoded to MM/DD/YYYY format. Updated to use the user's locale from their profile settings. Supports DD/MM/YYYY, YYYY-MM-DD, and other locale-specific formats. Fixed date parsing on backend too.
