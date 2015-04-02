from time import sleep
from ..fast import FastTrigger
from nio.common.signal.base import Signal
from nio.common.block.base import Block
from nio.modules.threading import Event
from nio.util.support.block_test_case import NIOBlockTestCase


class SampleFastBlock(FastTrigger, Block):
    pass


class TestFast(NIOBlockTestCase):

    def setUp(self):
        super().setUp()
        self.signals_out = 0
        self.notified = Event()

    def signals_notified(self, signals, output_id='default'):
        self.signals_out += len(signals)

    def throttled_generator(self, n):
        """ Return the correct number of signals - take it slow though """
        sleep(0.1)
        return [Signal() for i in range(n)]

    def test_fast(self):
        fast = SampleFastBlock()
        self.configure_block(fast, {
            'max_count': 100,
            'log_level': 'DEBUG'
        })
        fast.generate_signals = self.throttled_generator

        fast.start()
        # Go for a few seconds, we should see plenty of notifications
        sleep(2)
        fast.stop()

        # We should have had at least 10 notifications
        self.assertGreater(self.signals_out, 100 * 10)
        # Also, however many were notified should be a multiple of our count
        self.assertEqual(self.signals_out % 100, 0)

    def real_generator(self, n):
        """ Return the correct number of signals """
        try:
            return [Signal() for i in range(n)]
        finally:
            self.notified.set()

    def test_batch_size(self):
        """ Make sure odd batch sizes work too """
        fast = SampleFastBlock()
        fast.BATCH_SIZE = 37
        self.configure_block(fast, {
            'max_count': 100,
            'log_level': 'DEBUG'
        })
        fast.generate_signals = self.real_generator

        fast.start()
        # Just make it so we get at least one notification
        self.assertTrue(self.notified.wait(0.5))
        fast.stop()

        # Also, however many were notified should be a multiple of our count
        self.assertEqual(self.signals_out % 100, 0)
