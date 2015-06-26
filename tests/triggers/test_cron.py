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
        """ Test that signals are notified at midnight """
        blk = SampleCronBlock()
        self.configure_block(blk, {})
        returns = [Signal()]
        blk.generate_signals = MagicMock(return_value=returns)
        mock_dt.utcnow.side_effect = [datetime(2015, 6, 25, 0, 0)]
        blk.start()
        sleep(0.5)
        blk.stop()
        self.assert_num_signals_notified(1)

    @patch(CronTrigger.__module__ + '.datetime')
    def test_cron_match(self, mock_dt):
        """ Test that signals are notified at one minute after midnight """
        blk = SampleCronBlock()
        self.configure_block(blk, {
            "cron": {"minute": 1}
        })
        returns = [Signal()]
        blk.generate_signals = MagicMock(return_value=returns)
        mock_dt.utcnow.return_value = datetime(2015, 6, 25, 0, 1)
        blk.start()
        sleep(0.5)
        blk.stop()
        self.assert_num_signals_notified(1)

    @patch(CronTrigger.__module__ + '.datetime')
    def test_cron_no_match(self, mock_dt):
        """ Test that signals are not notified at midnight """
        blk = SampleCronBlock()
        self.configure_block(blk, {
            "cron": {"minute": 1}
        })
        returns = [Signal()]
        blk.generate_signals = MagicMock(return_value=returns)
        mock_dt.utcnow.return_value = datetime(2015, 6, 25, 0, 0)
        blk.start()
        sleep(0.5)
        blk.stop()
        self.assert_num_signals_notified(0)
