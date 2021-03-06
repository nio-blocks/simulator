FileIntervalSimulator
=====================
Creates signals as defined by a specified json file. The file must be a list of dictionaries where each dictionary is a nio Signal. The file should be loadable using `json.load`. Each call to generate_signals will return a signal from the list loaded in from the json file. When asked to generate -1 signals, it will generate all signals in the file. The block may be configured to read randomly from the file or sequentially.

Properties
---
- **Interval**: How often to emit generated signals.
- **Number of Signals**: How many signals get notified at once.
- **Choose Randomly?**: Whether or not to randomly pull from the file. If unchecked, the simulator will iterate through the file sequentially.
- **Signals File**: The location of the file containing a list of signals. It can be an absolute file location, relative to the root project directory or relative to the block path.
- **Total Number of Signals**: The maximum number of signals to emit overall. If less than 0 (-1 by default), then the trigger will continue to emit indefinitely until the block is stopped.

Commands
--------
 - **trigger** - Explicitly trigger the next signal to be notified. Note that triggering will ignore the rules of the block. It will not contribute to the max number of signals and it will still notify after the max has been hit. It will also always notify only one signal.
