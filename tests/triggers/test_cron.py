from unittest.mock import MagicMock, patch
from datetime import datetime
from time import sleep
from ...triggers.cron import CronTrigger
from nio.common.signal.base import Signal
from nio.common.block.base import Block
from nio.util.support.block_test_case import NIOBlockTestCase


class SampleCronBlock(CronTrigger, Block):
    pass


class TestCron(NIOBlockTestCase):

    def setUp(self):
        super().setUp()
        self.signals_out = 0

    def signals_notified(self, signals, output_id='default'):
        self.signals_out += len(signals)

    @patch(CronTrigger.__module__ + '.datetime')
    def test_default(self, mock_dt):
        """ Test that signals are notified at the right time """
        blk = SampleCronBlock()
        self.configure_block(blk, {})
        returns = [Signal()]
        blk.generate_signals = MagicMock(return_value=returns)
        mock_dt.utcnow.return_value = datetime(2015, 6, 25, 0, 0)

        # Give it enough time to complete two cycles - one right when the block
        # starts, the other after the first second has elapsed
        blk.start()
        sleep(1.5)
        blk.stop()

        self.assert_num_signals_notified(1)
