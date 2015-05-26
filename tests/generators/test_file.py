from unittest.mock import MagicMock
from ...generators.file import FileGenerator
from nio.common.block.base import Block
from nio.util.support.block_test_case import NIOBlockTestCase


class SampleFileBlock(FileGenerator, Block):
    pass


class TestFile(NIOBlockTestCase):

    def test_random_signals(self):
        blk = SampleFileBlock()
        blk._load_json_file = MagicMock(return_value=[{'a': 'A'}, {'b': 'B'}])
        self.configure_block(blk, {
            "random_selection": True
        })

        def _test_generate_signals(blk):
            results = list(blk.generate_signals())
            self.assertEqual(len(results), 1)
            try:
                # Check if the signal is the 'A' signal
                self.assertEqual(results[0].a, 'A')
            except:
                # If it's not 'A', then it better be 'B'
                self.assertEqual(results[0].b, 'B')

        # test a handful of gerations to check the randomness
        for _ in range(9):
            _test_generate_signals(blk)

    def test_sequential_signals(self):
        """ Make sure we iterate through the list and roll over """
        blk = SampleFileBlock()
        blk._load_json_file = MagicMock(return_value=[
            {'a': 'A'}, {'b': 'B'}, {'c': 'C'}])
        self.configure_block(blk, {
            "random_selection": False
        })

        four_signals = blk.generate_signals(n=4)
        self.assertEqual(len(four_signals), 4)
        self.assertEqual(four_signals[0].a, 'A')
        self.assertEqual(four_signals[1].b, 'B')
        self.assertEqual(four_signals[2].c, 'C')
        self.assertEqual(four_signals[3].a, 'A')

    def test_sequential_multiple_signals(self):
        """ Make sure we iterate through the list and roll over """
        blk = SampleFileBlock()
        blk._load_json_file = MagicMock(return_value=[
            {'a': 'A'}, {'b': 'B'}, {'c': 'C'}])
        self.configure_block(blk, {
            "random_selection": False
        })

        two_signals = blk.generate_signals(n=2)
        three_signals = blk.generate_signals(n=3)
        self.assertEqual(len(two_signals), 2)
        self.assertEqual(len(three_signals), 3)
        self.assertEqual(two_signals[0].a, 'A')
        self.assertEqual(two_signals[1].b, 'B')
        self.assertEqual(three_signals[0].c, 'C')
        self.assertEqual(three_signals[1].a, 'A')
        self.assertEqual(three_signals[2].b, 'B')

    def test_load_json_file_bad(self):
        blk = SampleFileBlock()
        with self.assertRaises(Exception):
            self.configure_block(blk, {})
        json_sigs = blk._load_json_file()
        self.assertIsNone(json_sigs)

    def test_load_json_file(self):
        blk = SampleFileBlock()
        self.configure_block(blk, {
            'signals_file': '../tests/generators/signals.json'
        })
        json_sigs = blk._load_json_file()
        self.assertEqual(len(json_sigs), 5)
