from .multiple import MultipleSignals
from .generators.counter import CounterGenerator
from .generators.identity import IdentityGenerator
from .generators.file import FileGenerator
from .triggers.interval import IntervalTrigger
from .triggers.safe import SafeTrigger
from .triggers.cron import CronTrigger
from nio import Block, discoverable
from nio.properties.version import VersionProperty


@discoverable
class CounterIntervalSimulator(
        MultipleSignals,
        CounterGenerator,
        IntervalTrigger,
        Block):

    version = VersionProperty('1.3.0')


@discoverable
class CounterSafeSimulator(
        CounterGenerator,
        SafeTrigger,
        Block):

    version = VersionProperty('1.1.0')


@discoverable
class IdentityIntervalSimulator(
        MultipleSignals,
        IdentityGenerator,
        IntervalTrigger,
        Block):

    version = VersionProperty('1.2.0')


@discoverable
class FileIntervalSimulator(
        MultipleSignals,
        FileGenerator,
        IntervalTrigger,
        Block):

    version = VersionProperty('1.3.0')


@discoverable
class IdentityCronSimulator(
        MultipleSignals,
        IdentityGenerator,
        CronTrigger,
        Block):

    version = VersionProperty('0.1.0')
