# Fix incorrect aggregation in monthly revenue reports

Revenue aggregation was double-counting prorated subscription changes. Fixed the calculation to use the subscription's effective date range and properly handle mid-month upgrades/downgrades. Added reconciliation check against Stripe.
