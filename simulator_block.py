from nio.common.block.base import Block
from nio.common.discovery import Discoverable, DiscoverableType
from .simulator_mixin import SimulatorMixin

@Discoverable(DiscoverableType.block)
class Simulator(SimulatorMixin, Block):
    def _simulate_signals(self, signal_count):
        """ Helper method to allow the simulations to happen in a thread.
        This allows the simulator to respond to the global state of its
        router.
        Args:
            None

        Returns:
            None

        """
        signals = [self._create_signal() for _ in range(signal_count)]
        self.notify_signals(signals)
