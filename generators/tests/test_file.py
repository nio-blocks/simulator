from unittest.mock import MagicMock
from ..file import FileGenerator
from nio.common.block.base import Block
from nio.util.support.block_test_case import NIOBlockTestCase


class SampleFileBlock(FileGenerator, Block):
    pass


class TestFile(NIOBlockTestCase):

    def test_generate_signals(self):
        blk = SampleFileBlock()
        blk._load_json_file = MagicMock(return_value=[{'a': 'A'}, {'b': 'B'}])
        self.configure_block(blk, {})

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

    def test_load_json_file_bad(self):
        blk = SampleFileBlock()
        self.configure_block(blk, {})
        json_sigs = blk._load_json_file()
        self.assertEqual(json_sigs, None)

    def test_load_json_file(self):
        blk = SampleFileBlock()
        self.configure_block(blk, {
            'signals_file': 'tests/signals.json'
        })
        json_sigs = blk._load_json_file()
        self.assertEqual(len(json_sigs), 5)
