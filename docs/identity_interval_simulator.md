IdentityIntervalSimulator
=========================
Simulates and notifies empty signals.

Properties
----------
- **interval**: How often to emit generated signals.
- **num_signals**: How many signals get notified at once.
- **total_signals**: The maximum number of signals to emit overall. If less than 0 (-1 by default), then the trigger will continue to emit indefinitely until the block is stopped.

Inputs
------
None

Outputs
-------
- **default**: The simulated signals.

Commands
--------
None
