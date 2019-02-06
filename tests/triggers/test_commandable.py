from unittest.mock import MagicMock
from nio import Signal, Block
from nio.util.discovery import not_discoverable
from nio.testing.block_test_case import NIOBlockTestCase

from ...triggers.commandable import CommandableTrigger


@not_discoverable
class SampleCommandableBlock(CommandableTrigger, Block):
    pass


class TestInterval(NIOBlockTestCase):

    def test_trigger_command(self):
        """ Interval trigger notifies all signals
        when total signals is not specified.
        """
        blk = SampleCommandableBlock()
        self.configure_block(blk, {})
        returns = [Signal({"num": 1})]
        blk.generate_signals = MagicMock(return_value=returns)

        blk.start()
        self.assertDictEqual(
            blk.trigger(), {
                "status": "triggered",
                "sigs": [{"num": 1}],
            })
        self.assert_num_signals_notified(1)
