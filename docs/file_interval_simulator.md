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
