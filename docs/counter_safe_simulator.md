CounterSafeSimulator
====================
Simulates and emits a signal containing an integer every [interval] seconds, even if not all signals have been simulated. The CounterSafeSimulator uses threading so that it can guarantee a notification every interval under heavy loads. If the 'max_count' is too high, the block will emit a signal with however many signals it was able to create during the defined interval. The signal can be named as needed. Multiple signals can be sent at each interval. The signal attribute may have an integer value that changes at each interval.

Properties
---
- **Simulated Attribute**: The name of the simulated signal attribute.
- **Simulated Value**: The value assigned to the simulated attribute.The value attached to the signal will begin with the start value and increase by the step value until reaching the end value. After reaching the end value, the next signal have the start value of the total number of signals have not been reached.
- **Interval**: How often to emit generated signals.
- **Max Count**: Maximum signals to emit. The block will never emit more signals than this count every interval. If the number is too high for it to create, it may emit less than this number. The only guarantee made by this block is that a notification will happen every interval.

Example
---
For a **CounterSafeSimulator** with `start=0, stop=12, step=3, and max_count = 3`
the output will be:
> **Note:** `*` is the point that the signals are notified
 ```
|------interval------|------interval------|------interval------|------interval------|
[ 0  3  6*             9 12  0*             3  6  9*            12  0  3*           ]
```