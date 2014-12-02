from nio.common.block.base import Block
from nio.common.discovery import Discoverable, DiscoverableType
from nio.modules.threading import Event, Lock
from .simulator_mixin import SimulatorMixin

@Discoverable(DiscoverableType.block)
class SimulatorSafe(SimulatorMixin, Block):
    def __init__(self):
        super().__init__()
        self._stop_event = Event()
        self._executing_lock = Lock()

    def _simulate_signals(self, signal_count):
        """ Helper method to allow the simulations to happen in a thread.
        This allows the simulator to respond to the global state of its
        router.
        Args:
            None

        Returns:
            None

        """
        count = 0
        signals = []

        # Stop any currently running simulator threads
        self._stop_event.set()
        # We only want one simulator thread simulating at a time
        with self._executing_lock:
            # Ok, we're running, so clear the event and wait
            self._stop_event.clear()
            while count < signal_count and not self._stop_event.is_set():
                signals.append(self._create_signal())
                count += 1
        # self._logger.debug("Min {0}, max {1}".format(_signals[0], _signals[-1]))
        # self._logger.debug("Notifying {0} signals".format(len(_signals)))
        self.notify_signals(signals)

    def stop(self):
        """ Stop the simulator thread.
        Overridden from the Block interface.

        """
        self._stop_event.set()
        super().stop()
