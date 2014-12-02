from .test_simulator import TestSimulator
from ..simulator_safe_block import SimulatorSafe

class TestSimulatorSafe(TestSimulator):
    Simulator = SimulatorSafe

