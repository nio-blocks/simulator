from nio import Block
from nio.properties.version import VersionProperty

from .multiple import MultipleSignals
from .generators.counter import CounterGenerator
from .generators.identity import IdentityGenerator
from .generators.file import FileGenerator
from .triggers.interval import IntervalTrigger
from .triggers.safe import SafeTrigger
from .triggers.cron import CronTrigger


class CounterIntervalSimulator(
        MultipleSignals,
        CounterGenerator,
        IntervalTrigger,
        Block):

    version = VersionProperty('1.3.0')


class CounterSafeSimulator(
        CounterGenerator,
        SafeTrigger,
        Block):

    version = VersionProperty('1.1.0')


class IdentityIntervalSimulator(
        MultipleSignals,
        IdentityGenerator,
        IntervalTrigger,
        Block):

    version = VersionProperty('1.2.0')


class FileIntervalSimulator(
        MultipleSignals,
        FileGenerator,
        IntervalTrigger,
        Block):

    version = VersionProperty('1.3.0')


class IdentityCronSimulator(
        MultipleSignals,
        IdentityGenerator,
        CronTrigger,
        Block):

    version = VersionProperty('0.1.0')
