from nio.common.block.base import Block
from nio.common.discovery import Discoverable, DiscoverableType
from nio.common.command import command
from nio.metadata.properties.int import IntProperty
from nio.metadata.properties.timedelta import TimeDeltaProperty
from nio.metadata.properties.object import ObjectProperty
from nio.common.signal.base import Signal
from nio.modules.threading import spawn, sleep, Event
from time import time as _time, sleep

import itertools

from .simulator_mixin import Attribute, CountTotal


def total_seconds(interval):
    return interval.days*24*60*60 + interval.seconds + interval.microseconds*1e-6


@command("value")
@Discoverable(DiscoverableType.block)
class SimulatorFast(Block):
    signal_count = IntProperty(default=1, title='Signal Count')
    interval = TimeDeltaProperty(title='Interval', default={'seconds': 1})
    attribute = ObjectProperty(Attribute, title='Attribute')
    count_total = ObjectProperty(CountTotal, title="Count Total")
    def __init__(self):
        super().__init__()
        self.counter = 0

    def start(self):
        super().start()
        self._stop_event = Event()
        spawn(self.simulate)

    def simulate(self):
        signal_count = self.signal_count
        count_range = self.attribute.value
        interval = total_seconds(self.interval)
        while True:
            start = _time()
            srange = iter(range(count_range.start, count_range.end + 1, count_range.step))
            while True:
                if self._stop_event.is_set():
                    return
                try:
                    signals = [n[1] for n in zip(range(signal_count), srange)]
                    self.notify_signals(signals)
                except StopIteration:
                    break
                try:
                    sleep(interval - (_time() - start))
                except ValueError:
                    pass

    def __simulate(self):
        islice = itertools.islice
        interval = total_seconds(self.interval)
        signal_count = self.signal_count
        count_total = self.count_total.count_total
        if count_total < 0:
            count_total = None
        reset_interval = self.count_total.reset_interval

        count_range = self.attribute.value
        srange = itertools.cycle(range(count_range.start, count_range.end + 1, count_range.step))
        name = self.attribute.name

        if signal_count <= 0:
            self._logger.error("Signal Count must be > 0")
            return

        self.counter = 0
        while(True):
            if count_total is None:
                count_left = signal_count
            else:
                count_left = count_total

            reset_start = _time()
            while count_left > 0:
                if self._stop_event.is_set():
                    break
                start = _time()
                dvals = ((n,) for n in zip(itertools.repeat(name), islice(islice(srange, signal_count), count_left)))
                dicts = map(dict, dvals)

                signals = list(map(Signal, dicts))
                len_sigs = len(signals)
                self.counter += len_sigs
                if count_total is not None:
                    count_left -= len_sigs

                self.notify_signals(signals)
                try:
                    sleep(interval - (_time() - start))
                except ValueError:
                    pass

            if reset_interval < 0:
                break  # never count again
            try:
                sleep_time = reset_interval - (_time() - reset_start)
                sleep(sleep_time)
            except ValueError:
                pass
            self.counter = 0

    def stop(self):
        self._stop_event.set()
        super().stop()

    def value(self):
        '''Access the total counted since last reset'''
        return self.counter
