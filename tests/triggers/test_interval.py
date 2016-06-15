from unittest.mock import MagicMock
from time import sleep
from ...triggers.interval import IntervalTrigger
from nio import Signal, Block
from nio.testing.block_test_case import NIOBlockTestCase
from ...multiple import MultipleSignals


class SampleIntervalBlock(IntervalTrigger, Block):
    pass

class TestInterval(NIOBlockTestCase):

    def test_interval_default(self):
        interval = SampleIntervalBlock()
        self.configure_block(interval, {
            'interval': {
                'seconds': 1
            }
        })
        returns = [Signal(), Signal()]
        interval.generate_signals = MagicMock(return_value=returns)

        interval.start()
        # Give it enough time for two notifications
        # (one immediately, one after a second)
        sleep(1.5)
        interval.stop()

        self.assert_num_signals_notified(4)

    def test_total_signals(self):
        interval = SampleIntervalBlock()
        self.configure_block(interval, {
            'interval': {
                'seconds': 1
            },
            'total_signals': 1
        })
        returns = [Signal()]
        interval.generate_signals = MagicMock(return_value=returns)

        interval.start()
        # Give it enough time for two notifications
        # but then the second one should not notify
        sleep(1.5)
        interval.stop()

        self.assert_num_signals_notified(1)

    def test_extra_generated_signals(self):
        interval = SampleIntervalBlock()
        self.configure_block(interval, {
            'interval': {
                'seconds': 0.1
            },
            'total_signals': 5
        })

        returns = [Signal(), Signal()]
        interval.generate_signals = MagicMock(return_value=returns)
        interval.start()
        sleep(0.5)
        interval.stop()

        self.assert_num_signals_notified(5)



















