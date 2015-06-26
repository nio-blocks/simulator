from datetime import datetime
from datetime import timedelta
from nio.metadata.properties import TimeDeltaProperty, IntProperty, \
    ObjectProperty, PropertyHolder, StringProperty
from nio.modules.scheduler import Job
from nio.modules.threading import Event, Lock, spawn


class CronConf(PropertyHolder):
    minute = IntProperty(title='Minute', default=1)
    hour = IntProperty(title='Hour', default=0)
    day_of_month = IntProperty(title='Day of Month', default=0)
    month = IntProperty(title='Month', default=0)
    day_of_week = IntProperty(title='Day of Week', default=0)


class CronTrigger():

    """ Notify signals accoriding to cron-like timetable """

    cron = ObjectProperty(CronConf, title='Cron Schedule', default=CronConf())

    def __init__(self):
        super().__init__()
        self._job = None
        self._cron_specs = None

    def configure(self, context):
        super().configure(context)
        # TODO: make this real. for now, default to midnight cron setting
        self._cron_specs = [0, 0, '*', '*', '*']

    def start(self):
        super().start()
        # Like crontab, check to run jobs every minute
        self._job = Job(self._cron, timedelta(minutes=1), True)
        # Run a cron cycle immediately, but in a new thread since it
        # might take some time and we don't want it to hold up start
        spawn(self._cron)

    def stop(self):
        """ Stop the simulator thread and signal generation """
        if self._job:
            self._job.cancel()
        super().stop()

    def _cron(self):
        """ Called every minute to check if cron job should nority signals """
        self._logger.debug("Checking if cron emit should run")
        now = datetime.utcnow()
        now = [now.minute, now.hour, now.day, now.month, now.weekday()]
        if self._check_cron(now):
            spawn(self._emit)

    def _check_cron(self, now):
        """ Return True if cron property matches with `now`

        `now` is list containing the 5 cron field
        """
        for i in range(5):
            # '*' should match no matter what
            if self._cron_specs[i] == '*':
                now[i] = '*'
        return now == self._cron_specs

    def _emit(self):
        self._logger.debug("Generating signals")
        signals = self.generate_signals()
        if signals:
            self._logger.debug("Notifying {} signals".format(len(signals)))
            self.notify_signals(signals)
        else:
            self._logger.debug("No signals generated")
