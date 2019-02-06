from nio.command import command
from nio.command.holder import CommandHolder


@command('trigger')
class CommandableTrigger(CommandHolder):
    """ A trigger that exposes a command to do the triggering.

    This can be used as a standalone trigger or can be a super class
    for another trigger which wishes to expose a command.

    Note that this trigger will ignore the rules of a trigger that inherits it.
    For example, if the IntervalTrigger was configured to only notify 1 signal,
    that count would not have any impact on this trigger. Signals could be
    triggered via the command after the max was exhausted and signals notified
    by this trigger would not increment that count.
    """

    def trigger(self):
        sigs = self.generate_signals(n=1)
        if not isinstance(sigs, list):
            sigs = list(sigs)
        self.notify_signals(sigs)
        return {
            "status": "triggered",
            "sigs": [sig.to_dict() for sig in sigs],
        }
