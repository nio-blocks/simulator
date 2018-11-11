CounterIntervalSimulator
========================
Simulates and emits a signal containing an integer every [interval] seconds. The signal can be named as needed. Multiple signals can be sent at each interval. The signal attribute may have an integer value that changes at each interval. If the total number of signals remaining is less than the number of signals to be emitted at the specified interval, the total number of signals remaining will be emitted.

Properties
----------
- **attr_name**: The name of the simulated signal attribute.
- **attr_value**: The value assigned to the simulated attribute.
- **interval**: How often to emit generated signals.
- **num_signals**: The amount of signals to emit at each interval.
- **total_signals**: The maximum number of signals to emit overall after the service starts. If less than 0 (-1 by default), then the trigger will continue to emit signals indefinitely until the block is stopped.

Inputs
------
None

Outputs
-------
- **default**: The simulated signals.

Commands
--------
None
