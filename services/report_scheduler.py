# Fix timezone handling in scheduled report delivery

Reports were being sent based on UTC timestamps instead of the customer's configured timezone. Fixed the scheduler to use customer timezone from their profile. Added timezone conversion tests for DST edge cases.
