import asyncio
import collections
import random
import chitchat as cc


def belly(prefix, target, message):
	lewd = ['N-no..', 'S-stop..', "T-that's lewd necro-nii-sama..", "If that's what you like..", 'P-please stop, t-that tickles..']
	return cc.privmsg(target, message=random.choice(lewd))

not_necro = lambda prefix, *args: prefix.nick != 'necromanteion'


def belly2(prefix, channel, message):
	return cc.kick(channel, prefix.nick, message="W-what do you think you're doing?!")
		

def paizuri(prefix, channel, message, cache=collections.defaultdict(lambda: 1)):	
	
	ban_time = cache[prefix.nick]
	cache[prefix.nick] *= 2
	
	yield cc.mode(channel, '+b', prefix.nick)
	yield cc.kick(channel, prefix.nick,
				  message='Banned for {0} second{1}!'.format(ban_time, 's' if ban_time > 1 else ''))
	
	yield from asyncio.sleep(ban_time)
	yield cc.mode(channel, '-b', prefix.nick)
	yield cc.invite(prefix.nick, channel)
	

def help(prefix, channel, message):
	helppls = ['Do ".rem" to roll on the Retarded Egg Machine!',
			   'Try ".paizuri" if you\'re a filthy perv!'] #all for now i guess
	return (cc.notice(prefix.nick, line) for line in helppls)