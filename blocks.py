from nio import GeneratorBlock
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
        GeneratorBlock):

    version = VersionProperty("1.2.1")


class CounterSafeSimulator(
        CounterGenerator,
        SafeTrigger,
        GeneratorBlock):

    version = VersionProperty("1.2.1")


class IdentityIntervalSimulator(
        MultipleSignals,
        IdentityGenerator,
        IntervalTrigger,
        GeneratorBlock):

    version = VersionProperty("1.2.1")


class FileIntervalSimulator(
        MultipleSignals,
        FileGenerator,
        IntervalTrigger,
        GeneratorBlock):

    version = VersionProperty("1.2.1")


class IdentityCronSimulator(
        MultipleSignals,
        IdentityGenerator,
        CronTrigger,
        GeneratorBlock):

    version = VersionProperty("1.2.1")
