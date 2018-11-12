CounterIntervalSimulator
========================
Simulates and emits a signal containing an integer every [interval] seconds. The signal can be named as needed. Multiple signals can be sent at each interval. The signal attribute may have an integer value that changes at each interval. If the total number of signals remaining is less than the number of signals to be emitted at the specified interval, the total number of signals remaining will be emitted.

Properties
----------
- **Simulated Attribute**: The name of the simulated signal attribute.
- **Simulated Value**: The value assigned to the simulated attribute.The value attached to the signal will begin with the start value and increase by the step value until reaching the end value. After reaching the end value, the next signal have the start value of the total number of signals have not been reached.
- **Interval**: How often to emit generated signals.
- **Number of Signals**: The amount of signals to emit at each interval.
- **Total Number of Signals**: The maximum number of signals to emit overall after the service starts. If less than 0 (-1 by default), then the trigger will continue to emit signals indefinitely until the block is stopped.
