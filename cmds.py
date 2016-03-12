import asyncio
import collections
import random
import string
import chitchat as cc


def bellyblocker(prefix, target, message):
    
    bellylist = ['belly', 'tummy', 'navelingus', 'nakadashi', 'ochinchin', 'bellyzuri',
                 'cum', 'midriff', 'cumdump', 'bully', 'dick', 'glistening',
                 'bellypillow', 'raspberry', 'tummies', 'bellies']
    
    normalized = ''.join(l for l in message if l in string.ascii_lowercase)
    
    return normalized in bellylist


def belly(prefix, target, message):
    lewd = ['N-no..', 'S-stop..', "T-that's lewd necro-nii-sama..",
            "If that's what you like..",
            'P-please stop, t-that tickles..']
    return cc.privmsg(target, message=random.choice(lewd))


not_necro = lambda prefix, *args: prefix.nick != 'necromanteion'

def belly2(prefix, channel, message):
    return cc.kick(channel, prefix.nick, message='{0.nick} no ecchi!'.format(prefix))
        

def paizuri(prefix, channel, message, cache=collections.defaultdict(lambda: 1)):
    
    ban_time = cache[prefix.nick]
    cache[prefix.nick] *= 2
    
    yield cc.mode(channel, '+b', prefix)
    yield cc.kick(channel, prefix.nick,
                  message='Banned for {0} second{1}!'.format(ban_time, 's' if ban_time > 1 else ''))
    
    yield from asyncio.sleep(ban_time)
    yield cc.mode(channel, '-b', prefix)
    yield cc.invite(prefix.nick, channel)
    

def help(prefix, channel, message):
    helppls = ['Do ".rem" to roll on the Retarded Egg Machine!',
               'Try ".paizuri" if you\'re a filthy perv!'] #all for now i guess
    return (cc.notice(prefix.nick, line) for line in helppls)

nicklist = ['Didac', 'necromanteion', 'FbW', 'WizardofOrz', 'Waah', 'Excorcism']

def kick(prefix, channel, message):
    _, *nicks = message.split()
    return cc.kick(channel, *nicks, message='Go away!')

sakuballList = ['Yes!', 'I think you shouldn\'t do that.', 'Kill yourself.', 'Maybe you should do another thing.', 'Yes! It will be fun!',
        'I think that will end up nicely. :3', 'Please give me some time to consider the answer.']

def sakuball(prefix, channel, message):
    return cc.privmsg(target, message='{0}: {1}'.format(prefix.nick, random.choice(sakuballList))
