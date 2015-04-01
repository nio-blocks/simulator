from .generators.counter import CounterGenerator
from .triggers.interval import IntervalTrigger
from nio.common.block.base import Block
from nio.common.discovery import Discoverable, DiscoverableType


@Discoverable(DiscoverableType.block)
class CounterIntervalSimulator(CounterGenerator, IntervalTrigger, Block):
    pass
