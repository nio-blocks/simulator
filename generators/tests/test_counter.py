from ...multiple import MultipleSignals
from ..counter import CounterGenerator
from nio.common.block.base import Block
from nio.util.support.block_test_case import NIOBlockTestCase


class SampleCounterBlock(CounterGenerator, Block):
    pass


class SampleCounterMultipleBlock(MultipleSignals, CounterGenerator, Block):
    pass


class TestCounter(NIOBlockTestCase):

    def test_counts(self):
        counter = SampleCounterBlock()
        self.configure_block(counter, {
            'attr_name': 'attr',
            'attr_value': {
                'start': 10,
                'end': 19,
                'step': 5
            }
        })
        results = counter.generate_signals(3)

        self.assertEqual(len(results), 3)
        self.assertEqual(results[0].attr, 10)
        self.assertEqual(results[1].attr, 15)
        # third one should have rolled over and started over at 10
        self.assertEqual(results[2].attr, 10)

    def test_multiple_counts(self):
        counter = SampleCounterMultipleBlock()
        self.configure_block(counter, {
            'attr_name': 'attr',
            'attr_value': {
                'start': 10,
                'end': 19,
                'step': 5
            },
            'num_signals': 2
        })
        # Don't call generate_signals with any arguments,
        # this is likely what the trigger will do and we want the
        # mix-in to specifiy how many signals to generate
        results = counter.generate_signals()

        self.assertEqual(len(results), 2)
        self.assertEqual(results[0].attr, 10)
        self.assertEqual(results[1].attr, 15)
