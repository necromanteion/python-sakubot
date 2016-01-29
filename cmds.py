import random

@chitchat.plugin(channel, nick, text='.belly')
def belly(self, channel, nick):
	if nick == necromanteion:
		lewd = ['N-no..', 'S-stop..', 'T-that\'s lewd necro-nii-sama..', 'If that\'s what you like..', 'P-please stop, t-that tickles..']
		return cc.privmsg(channel, nick, message=random.choice(lewd))
	else:
		return cc.kick(channel, nick, message='W-what do you think you\'re doing?!')
		
@chitchat.plugin(channel, nick, text='.paizuri')
def paizuri(self, channel, nick):
	return cc.kick(channel, nick, message='Too far.')
	
@chitchat.plugin(channel, nick, text='.help')
def help(self, channel, nick):
	helppls = ["Do .rem to roll on the Retarded Egg Machine!", "Do .padherder (name) to check someone\'s padherder or .padherder (name) (link) to get in yours!"] #all for now i guess
	return (cc.privmsg(channel, nick, helppls[i]) for i in helppls)  #no idea if werk