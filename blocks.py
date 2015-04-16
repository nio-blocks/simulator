from .multiple import MultipleSignals
from .generators.counter import CounterGenerator
from .generators.identity import IdentityGenerator
from .generators.file import FileGenerator
from .triggers.interval import IntervalTrigger
from .triggers.safe import SafeTrigger
from nio.common.block.base import Block
from nio.common.discovery import Discoverable, DiscoverableType
from nio.metadata.properties.version import VersionProperty


@Discoverable(DiscoverableType.block)
class CounterIntervalSimulator(
        MultipleSignals,
        CounterGenerator,
        IntervalTrigger,
        Block):

    version = VersionProperty('1.0.1')


@Discoverable(DiscoverableType.block)
class CounterSafeSimulator(
        CounterGenerator,
        SafeTrigger,
        Block):

    version = VersionProperty('1.0.1')


@Discoverable(DiscoverableType.block)
class IdentityIntervalSimulator(
        IdentityGenerator,
        IntervalTrigger,
        Block):

    version = VersionProperty('1.0.1')


@Discoverable(DiscoverableType.block)
class FileIntervalSimulator(
        FileGenerator,
        IntervalTrigger,
        Block):

    version = VersionProperty('1.0.1')
