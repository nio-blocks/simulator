# Simulator

A library of simulators as well as a framework for creating new types of signal simulators.

A simulator is a Block that is comprised of one Generator and one or more Triggers. In general, simulators can be "assembled" by using Python's multiple inheritance to make use of existing Generators and Triggers. In some cases, you may want to define your own Generator or Trigger, this is also documented below.

## Generators

Generators are responsible for one and only one thing: generating signals. They are classes that can utilize standard block methods (i.e. `start`, `configure`, etc) but the only requirement is that they define a `generate_signals` method. This method must accept one optional parameter, `n`. The implementation of `generate_signals` should return a list of `Signal` objects with length of list equal to `n`. 

Here is possibly the simplest implementation of a Generator - it will simply return empty signals:

```python
class IdentityGenerator():

    def generate_signals(self, n=1):
        return [Signal() for i in range(n)]
```

There is no guarantee that generators will get called from the same thread, so it is generally good practice to use `Lock` objects to make the generator thread safe. 

Generators likely will need to internally keep track of any additional variables used to generate the next signals (i.e. current value that increments, UPC codes to simulate, etc). 

### Existing Generators

#### CounterGenerator

Creates signals with one numeric attribute that will increment each time.

##### Properties

-   **attr_name**: The name of the attribute on the Signal
-   **attr_value**:
 -    **start**: Number that the simulator starts at
 -    **stop**: Number that the simulator stops at 
 -    **step**: Number that the simulator increments between each simulation
   -    Note: `start, stop, step = 0, 6, 3` will simulate `[0, 3, 6, 0]`


#### IdentityGenerator

Creates empty signals. This is most likely useful for driving some other type of Block that doesn't necessarily care about the signal contents, but rather that a signal has been notified.
