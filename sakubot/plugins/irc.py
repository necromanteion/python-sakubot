"""
Basic IRC commands for Sakubot.
"""

import chitchat as cc
from chitchat.constants import RPL_WELCOME
import os

from sakubot import sakubot


@sakubot.on('CONNECTED')
def identify(*args):
    """Identify nick and user with the server, send server password, and join channels."""
    yield cc.identify(nickname='Sakubot', username='v3a')
    # wait for the welcome message to know we've successfully joined
    yield from sakubot.wait_for(RPL_WELCOME)
    
    password = os.environ.get('RIZON_BOT')
    yield cc.privmsg('nickserv', 'identify {0}'.format(password))
    # wait for our password to be accepted so our vhost will show up
    yield from sakubot.wait_for('NOTICE', text='password accepted')
    
    yield cc.join('#sakubot', '#padg')


@sakubot.on('PING')
def pong(prefix, target):
    return cc.pong(target)


@sakubot.on('DISCONNECTED')
def reconnect(host, port, exc=None):
    
    if exc:
        raise exc
    
    # reconnect to the server
    yield from sakubot.connect(host, port)


@sakubot.on('KICK', text='Sakubot')
def rejoin(prefix, channel, target, reason):
    return cc.join(channel)