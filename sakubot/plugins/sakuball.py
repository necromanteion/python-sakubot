import chitchat as cc
import random

from sakubot import sakubot

options = [
    # positive
    'Yes!',
    'Do it onii-chan!',
    'Sounds like fun!',
    'Best of luck onii-chan!',
    "It'll all work out okay!",
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
    "It can't be helped.",
    'You only live once, onii-chan.',
    "If you can do it tomorrow, don't do it today!",
    'Your life is in shambles, onii-chan.',
    "Sorry onii-chan I'm out of thumbs."
]


@sakubot.on('PRIVMSG', text=cc.operator.command('.sakuball'))
def sakuball(prefix, channel, message):
    
    line = '{0.nick}: {1}'.format(prefix, random.choice(options))
    
    return cc.privmsg(channel, line)