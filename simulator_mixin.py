from nio.metadata.properties.holder import PropertyHolder
from nio.metadata.properties.list import ListProperty
from nio.metadata.properties.object import ObjectProperty
from nio.metadata.properties.string import StringProperty
from nio.metadata.properties.int import IntProperty
from nio.metadata.properties.timedelta import TimeDeltaProperty
from nio.modules.scheduler import Job
from nio.common import get_class
import time


class Value(PropertyHolder):
    start = IntProperty(default=0, title='Start')
    end = IntProperty(default=1, title='End')
    step = IntProperty(default=1, title='Step')


class Attribute(PropertyHolder):
    name = StringProperty(default='sim', title='Name')
    value = ObjectProperty(Value, title='Value')


class CountTotal(PropertyHolder):
    count_total = IntProperty(default=-1, title="Total Count")
    reset_interval = IntProperty(default=-1, title="Reset Interval")


class SimulatorMixin(object):

    """ Simulator block.

    Generates a configurable number of configurable Signals at a
    configurable interval.

    Attributes:
        signal_type (StringProperty): Type of simulated signal,
            Defaults to 'nio.common.signal.base.Signal'.
        signal_count (IntProperty): Number of signals to generate
            per interval, defaults to 1.
        interval (TimeDeltaProperty): Time period of signal generation.

    """

    signal_type = StringProperty(default='nio.common.signal.base.Signal',
                                 title='Signal Type')
    signal_count = IntProperty(default=1, title='Signal Count')
    interval = TimeDeltaProperty(title='Interval', default={'seconds': 1})
    attributes = ListProperty(Attribute, default=[Attribute()],
                              title='Attributes')
    count_total = ObjectProperty(CountTotal, default=CountTotal(),
                                 title="Count Total")

    def __init__(self):
        """ Initializes the simulator

        """
        super().__init__()
        self._signal_class = object
        self._job = None
        self.attributes = []
        self.signal_count = 0
        self.total_signal_count = 0

    def _simulate_signals(self, signal_count):
        '''Override this method to enable simulation'''
        raise NotImplemented

    def _simulate(self):
        if self.count_total.count_total <= 0:
            self._simulate_signals(self.signal_count)
        # check if we have counted too much
        elif self.total_signal_count < self.count_total.count_total:
            diff = self.count_total.count_total - self.total_signal_count
            if diff >= self.signal_count:
                self._simulate_signals(self.signal_count)
            else:
                self._simulate_signals(diff)
        elif self.count_total.reset_interval < 0:
            pass  # never reset
        elif time.time() - self.last_reset >= self.count_total.reset_interval:
            self.total_signal_count = 0
            self.last_reset = time.time()
            self._simulate()  # we have reset, now we need to simulate again

    def configure(self, context):
        """ Configures attributes based on configuration.
        Overridden from the Block interface.

        Args:
            context: Block context

        Returns:
            None

        """

        super().configure(context)
        self._signal_class = get_class(self.signal_type)

    def start(self):
        """ Start simulating in a new thread.
        Overridden from the Block interface.

        Args:
            None

        Returns:
            None

        """
        super().start()
        self.last_reset = time.time()
        # initialize current with start value
        for attribute in self.attributes:
            setattr(attribute, "current", attribute.value.start)

        self._job = Job(self._simulate, self.interval, True)
        self._simulate()

    def _create_signal(self):
        """ Creates a signal and assigns attributes to it

        """
        self.total_signal_count += 1
        # TODO: for testing, take out soon
        assert(
            self.count_total.count_total <= 0 or
            self.total_signal_count <= self.count_total.count_total)

        signal = self._signal_class()
        for attribute in self.attributes:
            setattr(signal, attribute.name, attribute.current)
            self._save_next_value(attribute)
        return signal

    def _save_next_value(self, attribute):
        """ Saves the next attribute value to assign

        Args:
            attribute: Attribute to save value for

        """
        next_value = attribute.current + attribute.value.step
        if attribute.value.step > 0:
            # counting up
            if attribute.value.end != -1 and next_value > attribute.value.end:
                next_value = attribute.value.start
        else:
            # counting down
            if next_value < attribute.value.end:
                next_value = attribute.value.start

        attribute.current = next_value

    def stop(self):
        """ Stop the simulator thread.
        Overridden from the Block interface.

        """
        self._job.cancel()
        super().stop()
