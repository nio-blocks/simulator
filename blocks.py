from .multiple import MultipleSignals
from .generators.counter import CounterGenerator
from .triggers.interval import IntervalTrigger
from nio.common.block.base import Block
from nio.common.discovery import Discoverable, DiscoverableType
from nio.metadata.properties import VersionProperty


@Discoverable(DiscoverableType.block)
class CounterIntervalSimulator(
        MultipleSignals,
        CounterGenerator,
        IntervalTrigger,
        Block):

    version = VersionProperty('1.0.0')
