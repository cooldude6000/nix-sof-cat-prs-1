# Fix password reset emails not being sent for OAuth users

OAuth users (Google, GitHub SSO) had no password hash stored, so the password reset flow skipped them silently. Added a check to send a "set password" email instead of "reset password" for OAuth-only accounts.
