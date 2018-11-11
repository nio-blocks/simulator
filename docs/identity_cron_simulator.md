IdentityCronSimulator
=====================
Simulate and emit signals according to a cron-like timetable. At the specified time the block will emit the specified number of signals. Time may be specified using Year, Month, Day, Hour, and Minute. Timezone may be configured to UTC or local machine time.

Properties
----------
- **cron**: The time (UTC) at which to emit the simulated signals.
- **num_signals**: How many signals get notified at once.
- **utc**: Use UTC time or local time.

Inputs
------
None

Outputs
-------
- **default**: The simulated signals.

Commands
--------
None
