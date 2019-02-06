CounterIntervalSimulator
========================
Simulates and emits a signal containing an integer every [interval] seconds. The signal can be named as needed. Multiple signals can be sent at each interval. The signal attribute may have an integer value that changes at each interval.

Properties
---
- **Simulated Attribute**: The name of the simulated signal attribute.
- **Simulated Value**: The value assigned to the simulated attribute.The value attached to the signal will begin with the start value and increase by the step value until reaching the end value. After reaching the end value, the next signal have the start value of the total number of signals have not been reached.
- **Interval**: How often to emit generated signals.
- **Number of Signals**: The amount of signals to emit at each interval.
- **Total Number of Signals**: The maximum number of signals to emit overall after the service starts. If less than 0 (-1 by default), then the trigger will continue to emit signals indefinitely until the block is stopped.

Example
---
For a **CounterIntervalSimulator** with start=0, stop=12, step=3, and num_signals = 3,
the output will be:
> **Note:** `*` is the point that the signals are notified
```
|------interval------|------interval------|------interval------|------interval------|
[ 0  3  6*             9 12  0*             3  6  9*            12  0  3*           ]
```

Commands
--------
 - **trigger** - Explicitly trigger the next signal to be notified. Note that triggering will ignore the rules of the block. It will not contribute to the max number of signals and it will still notify after the max has been hit. It will also always notify only one signal.
