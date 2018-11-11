CounterIntervalSimulator
========================
Simulates and emits a signal every [interval] seconds.

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
