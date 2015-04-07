from nio.common.signal.base import Signal
from nio.modules.threading import Lock
from nio.metadata.properties import PropertyHolder, ObjectProperty, \
    IntProperty, StringProperty


class Value(PropertyHolder):
    start = IntProperty(default=0, title='Start')
    end = IntProperty(default=1, title='End')
    step = IntProperty(default=1, title='Step')


class CounterGenerator():

    attr_name = StringProperty(default='sim', title='Simulated Attribute')
    attr_value = ObjectProperty(Value, title='Simulated Value')

    def __init__(self):
        super().__init__()
        self.cur_count = 0
        self.count_lock = Lock()

    def configure(self, context):
        super().configure(context)
        # Initialize our count to the starting value
        self.cur_count = self.attr_value.start

    def generate_signals(self, n=1):
        return [self._get_next_signal() for i in range(n)]

    def _get_next_signal(self):
        """ Get the next signal we want to emit.

        This will update the cur_count and return a Signal with the current
        count at the time the function was called.
        """
        with self.count_lock:
            # store the current count, then increment it
            my_count = self.cur_count
            self._bump_count()

        return Signal({
            self.attr_name: my_count
        })

    def _bump_count(self):
        """ Increment the current count, roll over if necessary.

        Returns:
            None: self.cur_count gets updated instead
        """
        self.cur_count += self.attr_value.step
        if self.cur_count > self.attr_value.end:
            self.cur_count = self.attr_value.start
