import chitchat as cc
import random

from sakubot import sakubot

options = [
    # positive
    'Yes!',
    'Do it onii-chan!',
    'Sounds like fun!',
    '👍 Two thumbs up! 👍',
    # negative
    'No!',
    "Onii-chan I think that's a terrible mistake.",
    'Baka onii-chan, shine!',
    'Baka onii-chan, go away!',
    'Try something else, onii-chan.',
    '👎 Two thumbs down! 👎',
    # neutral
    'Hmm... Let me think about it.',
    'You only live once, onii-chan.',
    'Your life is in shambles, onii-chan.',
    "Sorry onii-chan I'm out of thumbs."
]


@sakubot.on('PRIVMSG', text=cc.operator.command('.sakuball'))
def sakuball(prefix, channel, message):
    
    line = '{0.nick}: {1}'.format(prefix, random.choice(options))
    
    return cc.privmsg(channel, line)