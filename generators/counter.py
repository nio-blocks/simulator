from itertools import chain, repeat

from nio.common.signal.base import Signal
from nio.modules.threading import Lock
from nio.metadata.properties import PropertyHolder, ObjectProperty, \
    IntProperty, StringProperty


class Value(PropertyHolder):
    start = IntProperty(default=0, title='Start')
    end = IntProperty(default=1, title='End')
    step = IntProperty(default=1, title='Step')


class CounterGenerator():
    '''A fast numeric batch generator'''

    attr_name = StringProperty(default='sim', title='Simulated Attribute')
    attr_value = ObjectProperty(Value, title='Simulated Value')

    def __init__(self):
        super().__init__()
        self.cur_count = 0
        self.count_lock = Lock()
        self._lasti = 0
        self.range = None

    def configure(self, context):
        super().configure(context)
        self._lasti = 0
        self.range = range(self.attr_value.start, self.attr_value.end + 1,
                           self.attr_value.step)

    def generate_signals(self, n=1):
        # bring variables into local space for minor speedup
        with self.count_lock:
            S = Signal
            myrange = self.range
            rlen = len(myrange)

            ranges = []
            sigs = 0
            # this is how much is left of the previously used range
            lasti = self._lasti
            while sigs < n:
                r = myrange[lasti: lasti + (n - sigs)]
                lasti = len(r) % rlen
                sigs += len(r)
                ranges.append(r)
            assert sigs == n
            self._lasti = lasti
            return (S({name: value}) for (name, value) in
                    zip(repeat(self.attr_name, sigs), chain.from_iterable(ranges)))
