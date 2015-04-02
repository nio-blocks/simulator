from nio.metadata.properties import IntProperty
from nio.modules.threading import Event, spawn


class FastTrigger():

    max_count = IntProperty(title="Number of Signals", default=1)

    # How many signals to generate at a time
    BATCH_SIZE = 10000

    def __init__(self):
        super().__init__()
        self._stop_event = Event()

    def start(self):
        super().start()
        spawn(self.run_signals)

    def run_signals(self):
        """ Create *max_count* signals and notify as fast as possible """
        # We are going to run until someone tells us to stop
        while not self._stop_event.is_set():
            # remaining will hold how many signals are left to create this run
            remaining = self.max_count
            signals = []

            # Check the stop event here too, so we can get out early
            while remaining > 0 and not self._stop_event.is_set():

                # Figure out how many more we have to create this batch
                if remaining > self.BATCH_SIZE:
                    to_create = self.BATCH_SIZE
                else:
                    to_create = remaining

                remaining -= to_create
                signals.extend(self.generate_signals(to_create))

            if self._stop_event.is_set():
                # Someone wants to stop, get out of this loop
                break
            else:
                # We just exhausted the loop, notify signals and do it again
                self._logger.debug("Notifying {} signals".format(len(signals)))
                self.notify_signals(signals)

    def stop(self):
        """ Stop the simulator thread. """
        self._stop_event.set()
        super().stop()
