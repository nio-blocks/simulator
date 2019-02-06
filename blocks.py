from nio import GeneratorBlock
from nio.properties.version import VersionProperty

from .multiple import MultipleSignals
from .generators.counter import CounterGenerator
from .generators.identity import IdentityGenerator
from .generators.file import FileGenerator
from .triggers.interval import IntervalTrigger
from .triggers.safe import SafeTrigger
from .triggers.cron import CronTrigger
from .triggers.commandable import CommandableTrigger


class CounterIntervalSimulator(
        MultipleSignals,
        CounterGenerator,
        IntervalTrigger,
        CommandableTrigger,
        GeneratorBlock):

    version = VersionProperty("1.5.0")


class CounterSafeSimulator(
        CounterGenerator,
        SafeTrigger,
        GeneratorBlock):

    version = VersionProperty("1.2.0")


class IdentityIntervalSimulator(
        MultipleSignals,
        IdentityGenerator,
        IntervalTrigger,
        CommandableTrigger,
        GeneratorBlock):

    version = VersionProperty("1.4.0")


class FileIntervalSimulator(
        MultipleSignals,
        FileGenerator,
        IntervalTrigger,
        CommandableTrigger,
        GeneratorBlock):

    version = VersionProperty("1.5.0")


class IdentityCronSimulator(
        MultipleSignals,
        IdentityGenerator,
        CronTrigger,
        CommandableTrigger,
        GeneratorBlock):

    version = VersionProperty("1.0.0")
