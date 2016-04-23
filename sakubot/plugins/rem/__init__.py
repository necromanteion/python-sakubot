import chitchat as cc
from sakubot import sakubot
from sakubot.plugins import paddb

from .events import DEFAULT, EVENTS
from .parsing import first_int, matches
from .structures import ErrorRaisingArgumentParser
from .utils import combine, percent


parser = ErrorRaisingArgumentParser(prog='.rem', add_help=False)
parser.add_argument('-n', default=1, type=int)

group = parser.add_mutually_exclusive_group(required=False)
group.add_argument('-c', '--chance', metavar='ID', type=int)
group.add_argument('-u', '--until', metavar='ID', type=int)


@sakubot.on('PRIVMSG', text='.rem')
def rem(prefix, target, message):
    
    try:
        flags, args = parser.parse_known_args(message.split())
    
    except ValueError:
        return usage(prefix, target)
    
    # build weighted rem from unparsed args
    rem = combine(combine(matches(arg, EVENTS), initializer=DEFAULT) for arg in args)
    
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
    # remove preceding 'usage: ' and concluding newline from parser's usage message
    line = line.format(prefix, ' '.join(parser.format_usage().strip().split()[1:]))
    
    return cc.privmsg(target, line)
    

def chance(prefix, target, event, card, n=1):
    """
    Calculate the percent chance of rolling `card` in `n` rolls of `event` and return a
    privmsg of the results.
    
    """
    
    chance = event.chance(card, n)
    
    line = 'You have a {0} chance of rolling {1} in {2} rolls of the {3.padded_title}REM.'
    line = line.format(percent(chance), paddb.name(card) or 'that monster', n, event)
    
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
                'the {1.padded_title}REM!')
        line = line.format(paddb.name(card) or 'that monster', event)
        return cc.privmsg(target, line)
    
    if n:
        line = 'It took me {0} rolls of the {1.padded_title}REM to roll {2}!'
        line = line.format(n, event, paddb.name(card) or 'that monster')
    
    else:
        line = "Sorry onii-chan, looks like you don't have enough stones for that."
        
    return cc.privmsg(target, line)


def roll(prefix, target, event, n=1):
    """Roll `n` times, yielding each result as an individual privmsg."""
        
    for card in event.roll(n):
        line = "{0.nick}-nii's {1.padded_title}REM roll: {2}!"
        line = line.format(prefix, event, paddb.name(card) or 'oops an error')
        yield cc.privmsg(target, line)