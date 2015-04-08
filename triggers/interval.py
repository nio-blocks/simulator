import time

from nio.metadata.properties import TimeDeltaProperty, BoolProperty, IntProperty
from nio.modules.threading import Event, spawn


class IntervalTrigger():
    '''Generate max_count signals every second up to total_signals'''

    max_count = IntProperty(title="Number of Signals", default=1)
    total_signals = IntProperty(title="Total Number of Signals", default=-1)
    interval = TimeDeltaProperty(title='Interval', default={'seconds': 1})
    notify_on_start = BoolProperty(
        title='Notify Immediately on Start', default=True)

    def __init__(self):
        super().__init__()
        self._stop_event = Event()
        self.counter = None

    def start(self):
        super().start()
        self.counter = 0
        self._stop_event.clear()
        # import pdb; pdb.set_trace()
        # self.run()
        spawn(self.run)

    def run(self):
        # pull into local namespace for speed
        ttime = time.time
        tsleep = time.sleep
        sigs_left = int(self.total_signals) if self.total_signals > 0 else None
        max_count = int(self.max_count)
        interval = self.interval.total_seconds()

        if not self.notify_on_start:
            tsleep(interval)

        start = ttime()
        while not self._stop_event.is_set():
            if sigs_left is None or sigs_left > max_count:
                to_gen = max_count
            else:
                to_gen = sigs_left
            sigs = self.generate_signals(to_gen)
            if not isinstance(sigs, list):
                sigs = list(sigs)
            self.notify_signals(sigs)
            self.counter += to_gen
            if sigs_left is not None:
                sigs_left -= to_gen
                if sigs_left <= 0:
                    break

            # sleep the exact correct amount of time
            try:
                sleep_start = ttime()
                tosleep = interval - (sleep_start - start)
                tsleep(tosleep)
                over = tosleep - (ttime() - sleep_start)
            except ValueError:
                over = 0
            start = ttime() + over

    def stop(self):
        """ Stop the simulator thread. """
        self._stop_event.set()
        super().stop()
