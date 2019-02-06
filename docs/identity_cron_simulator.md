IdentityCronSimulator
=====================
Simulate and emit signals according to a cron-like timetable. At the specified time the block will emit the specified number of signals. Time may be specified using Year, Month, Day, Hour, and Minute. Timezone may be configured to UTC or local machine time.

Properties
---
- **Cron Schedule**: The time (UTC) at which to emit the simulated signals.
- **Number of Signals**: How many signals get notified at once.

Advanced Properties
---
- **UTC**: Select to use UTC time instead of local machine time.

Commands
--------
 - **trigger** - Explicitly trigger the next signal to be notified. Note that triggering will ignore the rules of the block. It will not contribute to the max number of signals and it will still notify after the max has been hit. It will also always notify only one signal.
