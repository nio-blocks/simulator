from time import time, sleep

from nio.properties import TimeDeltaProperty, IntProperty
from nio.util.threading import spawn
from threading import Event


class IntervalTrigger():
    '''Generate signals at a regular interval up to total_signals'''

    total_signals = IntProperty(title="Total Number of Signals", default=-1)
    interval = TimeDeltaProperty(title='Interval', default={'seconds': 1})

    def __init__(self):
        super().__init__()
        self._stop_event = Event()
        self.counter = None

    def start(self):
        super().start()
        self.counter = 0
        self._stop_event.clear()
        spawn(self.run)

    def run(self):
        # We'll keep track of when each iteration is expected to finish
        interval_secs = self.interval().total_seconds()
        expected_finish = time() + interval_secs

        while not self._stop_event.is_set():
            sigs = self.generate_signals()

            # If a generator is returned, build the list
            if not isinstance(sigs, list):
                sigs = list(sigs)

            # Add however many signals were generated (in case multiple
            # signals mixin was used) to the counter and notify them
            self.counter += len(sigs)
            
            #check to see if counter > total_signals
            #if true, then pop list (counter - total_signals)
            #amount of times
            if self.counter > self.total_signals() and self.total_signals() >= 0:
                #self.counter - self.total_signals() yield that amount of signals that should be removed
                sigs_to_remove = self.counter - self.total_signals()
                sigs = sigs[:-1 * sigs_to_remove]

            self.notify_signals(sigs)

            if self.total_signals() > 0 and \
                    self.counter >= self.total_signals():
                # We have reached our total, stop
                break

            # sleep the exact correct amount of time
            time_remaining = expected_finish - time()
            if time_remaining > 0:
                # If we have time remaining, sleep until the next iteration
                sleep(time_remaining)

            # One iteration is complete, increment our next "expected finish"
            # time. This expected_finish could fall behind the actual time
            # if it takes longer than interval_secs to generate the signals
            expected_finish += interval_secs

    def stop(self):
        """ Stop the simulator thread. """
        self._stop_event.set()
        super().stop()
