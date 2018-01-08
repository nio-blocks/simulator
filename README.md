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

FileIntervalSimulator
=====================
Creates signals as defined by a json file. The file must be a list of dictionaries where each dictionary is a nio Signal. The file should be loadable using `json.load`.  Each call to generate_signals will return a signal from the list loaded in from the json file.  When asked to generate -1 signals, it will generate all signals in the file.

Properties
----------
- **interval**: How often to emit generated signals.
- **num_signals**: How many signals get notified at once.
- **random_selection**: Whether or not to randomly pull from the file. If unchecked, the simulator will iterate through the file sequentially.
- **signals_file**: The location of the file containing a list of signals. It can be an absolute file location, relative to the root project directory or relative to the block path.
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

IdentityCronSimulator
=====================
Simulate and emit signals according to a cron-like timetable

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

