import random
import chitchat as cc

@cc.on(nick='necromanteion', text='.belly')
def belly(prefix, target, message):
	lewd = ['N-no..', 'S-stop..', "T-that's lewd necro-nii-sama..", "If that's what you like..", 'P-please stop, t-that tickles..']
	return cc.privmsg(target, message=random.choice(lewd))

not_necro = lambda prefix, *args: prefix.nick != 'necromanteion'

@cc.on(nick=not_necro, text='.belly')
def belly2(prefix, channel, message):
	return cc.kick(channel, prefix.nick, message="W-what do you think you're doing?!")
		
@cc.plugin(channel, nick, text='.paizuri')
def paizuri(prefix, channel, message):
	return cc.kick(channel, prefix.nick, message='Too far.')
	
@cc.plugin(text='.help')
def help(prefix, channel, message):
	helppls = ["Do .rem to roll on the Retarded Egg Machine!", "Do .padherder (name) to check someone\'s padherder or .padherder (name) (link) to get in yours!"] #all for now i guess
	return (cc.privmsg(prefix.nick, help) for help in helppls)
