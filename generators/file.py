import json
import random
from os.path import join, dirname, realpath, isfile
from nio.common.signal.base import Signal
from nio.modules.threading import Lock
from nio.metadata.properties import StringProperty
from nio.util.environment import NIOEnvironment


class FileGenerator():
    '''A generator that pull signals from a file'''

    signals_file = StringProperty(
        title='Signals File', default='signals.json')

    def __init__(self):
        super().__init__()
        self._json_signals = None
        self._num_signals = 0

    def configure(self, context):
        super().configure(context)
        self._json_signals = self._load_json_file()
        self._num_signals = len(self._json_signals) \
            if self._json_signals else 0
        self._logger.debug(
            'Loaded {} signals from file'.format(self._num_signals))

    def generate_signals(self, n=1):
        if self._num_signals:
            return [Signal(random.choice(self._json_signals))]
        else:
            return []

    def _load_json_file(self):
        '''Loads the configured JSON file with signals

        Returns json file or None if failed to load file.
        '''

        # Let's figure out where the file is
        filename = self._get_valid_file(
            # First, just see if it's maybe already a file?
            self.signals_file,
            # Next, try in the NIO environment
            NIOEnvironment.get_path(self.signals_file),
            # Finally, try relative to the current file
            join(dirname(realpath(__file__)), self.signals_file),
        )

        if filename is None:
            self._logger.error(
                'Could not find key file {0}. Should be an absolute path or '
                'relative to the current environment.'.format(
                    self.signals_file))
            return None
        else:
            self._logger.info('Loading signals from file: {}'.format(filename))

        with open(filename) as json_file:
            try:
                json_data = json.load(json_file)
                return json_data
            except:
                self._logger.exception('Failed to load json signals file')

    def _get_valid_file(self, *args):
        '''Go through args and return the first valid file.

        Returns None if none no valid file is found.
        '''
        for arg in args:
            if isfile(arg):
                return arg
        return None
