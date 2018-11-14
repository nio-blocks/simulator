IdentityIntervalSimulator
=========================
Simulates and emits an empty signal ```{}``` at each specified interval. The block may be configured to notify any number of signals at the interval. The total number of signals for the block to emit is also configurable. If the total number of signals remaining is less than the number of signals expected to be emitted at the interval, the block will emit the total number remaining.

Properties
---
- **Interval**: How often to emit generated signals.
- **Number of Signals**: How many signals get emitted at each interval.
- **Total Number of Signals**: The maximum number of signals to emit overall. If less than 0 (-1 by default), then the trigger will continue to emit indefinitely until the block is stopped.
