import chitchat as cc
import inflect
from sakubot import sakubot
from sakubot.plugins import paddb

from .events import DEFAULT, EVENTS
from .parsing import first_int, matches
from .structures import ErrorRaisingArgumentParser
from .utils import combine, percent

engine = inflect.engine()

parser = ErrorRaisingArgumentParser(prog='.rem', add_help=False)
parser.add_argument('-n', default=1, type=int)

group = parser.add_mutually_exclusive_group(required=False)
group.add_argument('-c', '--chance', metavar='ID', type=int)
group.add_argument('-u', '--until', metavar='ID', type=int)


@sakubot.on('PRIVMSG', text=cc.operator.command('.rem'))
def rem(prefix, target, message):
    
    try:
        flags, args = parser.parse_known_args(message.split())
    
    except ValueError:
        return usage(prefix, target)
    
    # build weighted rem from unparsed args
    rem = combine(combine(matches(arg, EVENTS) for arg in args), initializer=DEFAULT)
    
    if flags.chance:
        return chance(prefix, target, event=rem, card=flags.chance, n=flags.n)
    
    elif flags.until:
        return until(prefix, target, event=rem, card=flags.until)
    
    return roll(prefix, target, event=rem, n=min(flags.n, 5))


def usage(prefix, target):
    """
    Return a generic usage message on error.
    """
    
    line = '{0.nick} no baka! Use it like this: {1} [event [event ...]]'
    line = line.format(prefix, parser.format_usage())
    
    return cc.privmsg(target, line)
    

def chance(prefix, target, event, card, n=1):
    """
    Calculate the percent chance of rolling `card` in `n` rolls of `event` and return a
    privmsg of the results.
    """
    
    chance = event.chance(card, n=n)
    
    line = 'You have a {0} chance of rolling {1} in {2} {3} of the {4.formatted_title}.'
    line = line.format(
        percent(chance),
        paddb.name(card) or 'that monster',
        engine.number_to_words(n, threshold=100),
        engine.plural('roll', n),
        event
    )
    
    return cc.privmsg(target, line)


def until(prefix, target, event, card):
    """
    Roll in `event` until `card` is found and return a privmsg of the number of rolls
    necessary.
    """
    
    try:
        n = event.roll_until(card)
    
    except ValueError:
        line = ("Onii-chan your fat, greasy fingers must've made a typo, {0} isn't in "
                'the {1.formatted_title}!')
        line = line.format(paddb.name(card) or 'that monster', event)
        return cc.privmsg(target, line)
    
    if n:
        line = 'It took me {0} {1} of the {2.formatted_title} to roll {3}!'
        line = line.format(
            engine.number_to_words(n, threshold=100),
            engine.plural('roll', n),
            event,
            paddb.name(card) or 'that monster'
        )
    
    else:
        line = "Sorry onii-chan, looks like you don't have enough stones for that."
        
    return cc.privmsg(target, line)


def roll(prefix, target, event, n=1):
    """Roll `n` times, yielding each result as an individual privmsg."""
        
    for card in event.roll(n):
        line = "{0.nick}-nii's {1.formatted_title} roll: (#{2}) {3}!"
        line = line.format(prefix, event, card, paddb.name(card) or 'some monster')
        yield cc.privmsg(target, line)