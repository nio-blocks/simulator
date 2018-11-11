CounterSafeSimulator
====================
Simulates and emits a signal every [interval] seconds, even if not all signals have been simulated.  If the 'max_count' is too high, the block will emit a signal with however many signals it was able to create during the defined interval.

Properties
----------
- **attr_name**: The name of the simulated signal attribute.
- **attr_value**: The value assigned to the simulated attribute.
- **interval**: How often to emit generated signals.
- **max_count**: Maximum signals to emit. The block will never emit more signals than this count every interval. If the number is too high for it to create, it may emit less than this number. The only guarantee made by this block is that a notification will happen every interval.

Inputs
------
None

Outputs
-------
- **default**: The simulated signals.

Commands
--------
None
