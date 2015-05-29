from unittest.mock import MagicMock
from time import sleep
from ...triggers.interval import IntervalTrigger
from nio.common.signal.base import Signal
from nio.common.block.base import Block
from nio.util.support.block_test_case import NIOBlockTestCase


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
