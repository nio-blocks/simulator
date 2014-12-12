from nio.modules.threading import sleep
from nio.util.support.block_test_case import NIOBlockTestCase
from nio.modules.scheduler import SchedulerModule
from ..simulator_fast_block import SimulatorFast

num_signals_per_interval = 2
interval_duration_secs = 1
config = {
    "signal_count": num_signals_per_interval,
    "interval": {
        "seconds": interval_duration_secs,
    },
    "attribute": {"name": "CounterBy2", "value": {"start": 1,
                                                    "end": 1,
                                                    "step": 2}},
    "count_total": {"count_total": num_signals_per_interval * 3,
                    "reset_interval": interval_duration_secs * 5,},
}

class TestSimulator(NIOBlockTestCase):

    Simulator = SimulatorFast

    def test_simulate(self):
        """Test that the simulator simulates and keeps a good interval.

        The simulator starts notifying signals only after a full interval
        has passed. As such, waiting for 2.5 full intervals should have
        notified two sets of signals.
        """
        print("Testing:", self.Simulator.__name__)
        sim = self.Simulator()

        self.configure_block(sim, config)

        sim.start()

        # Should have num_signals after duration + 0.5 seconds
        sleep(0.5) # waited 0.5
        self.assert_num_signals_notified(num_signals_per_interval, sim)

        # After interval_duration seconds we should have 2*num_signals
        sleep(interval_duration_secs) # waited 1.5
        self.assert_num_signals_notified(2 * num_signals_per_interval, sim)

        # Assert that no other signals were generated either
        self.assert_num_signals_notified(2 * num_signals_per_interval)

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
