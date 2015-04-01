from ...multiple import MultipleSignals
from ..identity import IdentityGenerator
from nio.common.block.base import Block
from nio.util.support.block_test_case import NIOBlockTestCase


class SampleIdentityBlock(IdentityGenerator, Block):
    pass


class SampleIdentityMultipleBlock(MultipleSignals, IdentityGenerator, Block):
    pass


class TestIdentity(NIOBlockTestCase):

    def test_counts(self):
        identity = SampleIdentityBlock()
        results = identity.generate_signals(3)

        self.assertEqual(len(results), 3)

    def test_multiple_counts(self):
        identity = SampleIdentityMultipleBlock()
        self.configure_block(identity, {
            'num_signals': 2
        })
        # Don't call generate_signals with any arguments,
        # this is likely what the trigger will do and we want the
        # mix-in to specifiy how many signals to generate
        results = identity.generate_signals()

        self.assertEqual(len(results), 2)
