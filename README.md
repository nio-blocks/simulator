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


## Triggers

A Trigger's job is to determine when signals should be generated and notified. There is no strictly defined interface for a Trigger's implementation, but it will almost certainly need to call `self.generate_signals()` at some point to be effective. Just like a Generator, the Trigger can define functionality inside standard block methods (just make sure to call `super()` in the implementation!). The Trigger is also responsible for notifying the signals, so it will likely make some `self.notify_signals` calls as well. 

Here is an example of a Trigger that will generate signals every second. Note: don't use this Trigger, it won't respond to block stop events, it's just an example:

```python
class OneSecondTrigger():

    def start(self):
        super().start()
        while True:
            self.notify_signals(self.generate_signals())
            sleep(1)
```

### Existing Triggers

#### IntervalTrigger

Notifies signals every interval.

##### Properties

-   **notify_on_start**: Whether or not to immediately notify simulated signals
-   **interval**: How often should the block notify signals
