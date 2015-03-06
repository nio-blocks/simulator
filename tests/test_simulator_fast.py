from copy import deepcopy
from nio.modules.threading import sleep
from nio.util.support.block_test_case import NIOBlockTestCase
from nio.modules.scheduler import SchedulerModule
from ..simulator_fast_block import SimulatorFast

num_signals_per_interval = 5
interval_duration_secs = 1
start, end, step = 1, 11, 1
config = {
    "name": 'simulator',
    "signal_count": num_signals_per_interval,
    "interval": {
        "seconds": interval_duration_secs,
    },
    "attribute": {"name": "sim", "value": {"start": start,
                                           "end": end,
                                           "step": step}},
    "count_total": {"count_total": num_signals_per_interval * 3,
                    "reset_interval": interval_duration_secs * 5},
}

class TestSimulator(NIOBlockTestCase):

    Simulator = SimulatorFast

    def setUp(self):
        super().setUp()
        self.signals = []

    def signals_notified(self, signals, output_id="default"):
        self.signals.extend(signals)

    def test_simulate(self):
        """Test that the simulator simulates and keeps a good interval.

        The simulator starts notifying signals only after a full interval
        has passed. As such, waiting for 2.5 full intervals should have
        notified two sets of signals.
        """
        print("Testing:", self.Simulator.__name__)
        self.signals.clear()
        sim = self.Simulator()
        self.configure_block(sim, config)
        sim.start()

        # Should have num_signals after duration + 0.5 seconds
        sleep(0.5) # waited 0.5
        self.assert_num_signals_notified(num_signals_per_interval, sim)

        # After interval_duration seconds we should have 2*num_signals
        sleep(interval_duration_secs)  # waited 1.5
        self.assert_num_signals_notified(2 * num_signals_per_interval, sim)

        # Assert that no other signals were generated either
        self.assert_num_signals_notified(2 * num_signals_per_interval, sim)

        # assert that we get our full output of signals
        sleep(interval_duration_secs) # waited 2.5
        self.assert_num_signals_notified(3 * num_signals_per_interval, sim)

        # assert that we get no more signals in the next duration
        sleep(interval_duration_secs) # waited 3.5
        self.assert_num_signals_notified(3 * num_signals_per_interval, sim)

        # sleep for 2 more intervals, we should have reset and got one more set
        sleep(interval_duration_secs * 2) # waited 5.5
        self.assert_num_signals_notified(4 * num_signals_per_interval, sim)

        sim.stop()

    def test_wrap(self):
        myconfig = deepcopy(config)
        myconfig["count_total"] = {"count_total": -1, "reset_interval": -1}
        self.signals.clear()
        sim = self.Simulator()
        self.configure_block(sim, myconfig)

        sim.start()

        # Should have num_signals after duration + 0.5 seconds
        sleep(2.5)  # waited 0.5
        self.assert_num_signals_notified(num_signals_per_interval * 3, sim)
        result = [s.sim for s in self.signals]
        exrange = range(start, end + 1, step)
        expected = list(exrange) + list(exrange[
            :num_signals_per_interval - len(exrange) - 1])
        self.assertListEqual(expected, result)

