# Fix SAML token refresh logic dropping active sessions

The SAML assertion consumer was not refreshing tokens before expiry. Added a 5-minute buffer window for token refresh and fixed the session store to preserve active sessions during refresh cycles.
