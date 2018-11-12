IdentityCronSimulator
=====================
Simulate and emit signals according to a cron-like timetable. At the specified time the block will emit the specified number of signals. Time may be specified using Year, Month, Day, Hour, and Minute. Timezone may be configured to UTC or local machine time.

Properties
----------
- **Cron Schedule**: The time (UTC) at which to emit the simulated signals.
- **Number of Signals**: How many signals get notified at once.

Advanced Properties
---
- **UTC**: Select to use UTC time instead of local machine time.
