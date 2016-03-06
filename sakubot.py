import asyncio
import random
import os
import chitchat as cc

import cmds
import padx_parser as pdx

sakubot = cc.Client()

# register plugins
sakubot.on(nick='necromanteion', text=cc.firstword('.belly'))(cmds.belly)
sakubot.on(text=lambda _, __, msg: msg.strip(''.join(ord(i) for i in range(33))).split()[0] in bellylist)
sakubot.on(text=cc.firstword('.paizuri'))(cmds.paizuri)
sakubot.on(text=cc.firstword('.help'))(cmds.help)
sakubot.register('PRIVMSG', cmds.kick, text=cc.firstword('kick'))
sakubot.on(text=cc.firstword('.compare'))(pdx.compare)

@sakubot.on('connected')
def identify(*args):
    """Identify nick and user with the server, send server password, and join channels."""
    yield cc.identify(nickname='Sakubot', username='v3')
    
    # wait for the welcome message to know we've successfully joined
    yield from sakubot.wait_for(cc.constants.RPL_WELCOME)
    
    password = os.environ.get('RIZON_BOT')
    yield cc.privmsg('nickserv', 'identify {0}'.format(password))
    
    # wait for our password to be accepted so our vhost will show up
    yield from sakubot.wait_for('NOTICE', text='password accepted')
    
    yield cc.join('#sakubot', '#padg')


@sakubot.on('ping')
def pong(prefix, target):
    return cc.pong(target)


@sakubot.on('PRIVMSG', text=cc.firstword('.rem'))
def rem(prefix, target, text):    
    mons = 'Sakuya Meimei Leilan Haku Karin Artemis Freyja LKali DKali Salamanderbelly'.split()
    line = 'You rolled a {0}, {1}-nii!'.format(random.choice(mons), prefix.nick)        
    
    return cc.privmsg(target, line)
    
    
@sakubot.on(text='.quit', nick='necromanteion')
def quit(*args):
    yield cc.quit()
    
    # if you're using BaseEventLoop.run_forever, BaseEventLoop.stop should be called
    # somewhere in a function called upon disconnecting from the server to stop release
    # the blocking call
    sakubot.loop.stop()


@sakubot.on('kick', text='Sakubot')
def rejoin(prefix, channel, target, reason):
    return cc.join(channel)
    

@sakubot.on('DISCONNECTED')
async def reconnect(host, port, exc):
    await sakubot.connect(host=host, port=port)
    
    
@sakubot.on(cc.constants.ALL)
def log(*args):
    print(*args)
   
    
if __name__ == '__main__':
    sakubot.run(host='irc.rizon.net', port=6667)
