from nio.metadata.properties import TimeDeltaProperty, BoolProperty
from nio.modules.scheduler import Job


class IntervalTrigger():

    interval = TimeDeltaProperty(title='Interval', default={'seconds': 1})
    notify_on_start = BoolProperty(
        title='Notify Immediately on Start', default=True)

    def __init__(self):
        super().__init__()
        self._job = None

    def start(self):
        super().start()
        self._job = Job(self._simulate, self.interval, True)
        if self.notify_on_start:
            self._simulate()

    def stop(self):
        """ Stop the simulator thread. """
        if self._job:
            self._job.cancel()
        super().stop()

    def _simulate(self):
        self._logger.debug("Triggering signals")
        out = self.generate_signals()
        if not isinstance(out, list):
            out = list(out)
        self.notify_signals(out)
