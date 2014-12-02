Simulator
===========

Generates a configurable number of configurable Signals at a configurable interval.

When **value** is counting up, **end** = -1 will count forever.

Properties
--------------

-   **attributes**: List of attribute names and values to add to output signals.
 -    **start**: Number that the simulator starts at
 -    **stop**: Number that the simulator stops at 
   -    Note: `start, stop, step = 0, 5, 1` will simulate `[0,1,2,3,4,5]`
 -    **step**: Number that the simulator skips between each simulation
-   **interval**: Period at which to notify signals.
-   **signal_count**: Number of signals to notify each *interval*.
-   **Count Total**
  -   **Total Count**: Total number of signals that the simulator will simulate. After this number has been reached, the simulator will stop (permanatly if not reset by **Reset Interval**).
    - if **Total Count** <= 0, it is ignored (simulator will simulate indefinately)
  -   **Reset Interval**: Time from *begginning of simulation* that a reset will occur.
    - if the simulation takes longer than **Reset Interval**, the simulator will be reset immediately after **Total Count** has been reached.
    - if **Reset Interval** < 0 the simulator will never be reset, i.e. it will count to Total Count and then stop indefinitely (until the service is restarted)
-   **signal_type**: Signal type. Defaults to 'nio.common.signal.base.Signal'.


Dependencies
----------------
None

Commands
----------------
None

Input
-------
None

Output
---------
New simulated signals.

---------

SimulatorSafe
===========
Exactly the same as Simulator, except if the number of signals requested cannot be generated in the given *interval*, then SimulatorSafe will stop generating signals (and start generating signals in the new interval).

For example, in an extremely slow system the simulations could look like:
```
# Simulator (start = 0, stop = 30, step = 1)
| <- interval ->  | <- interval ->  | <- interval ->  |
 00 01 02 03 04 05 06 08 10 12 14 16 18 21 24 27 30 02 # Each line continues until
                   07 09 11 13 15 17 19 22 25 28 00 03 #   30 signals have been 
                                     20 23 26 29 01 04 #   generated in that line

# SimulatorSafe (start = 0, stop = 30, step = 1)
| <- interval ->  | <- interval ->  | <- interval ->  |
 00 01 02 03 04 05 
                   06 07 08 09 10 11
                                     12 13 14 15 16 17
```

As you can see, SimulatorSafe may generate less signals (not tested), but it will always:
- Output a list of signals every second (the standard simulator may take longer)
- These signals will always be ordinal. As you can see above, the standard Simulator's signals were not ordinal when it could not generate fast enough
