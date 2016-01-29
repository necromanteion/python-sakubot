import chitchat

#@chitchat.plugin(text='.rem')
async def command(prefix, target, message):

    # parse number of rolls and specified godfests
    # n should default to 1 and have an upper limit
    # n, params = parse(message)

    return (chitchat.reply(roll(params)) for i in range(n))
#if you keep this thing above  ^  change all returns
pantheons=["pantheons here"]
#@cc.whatever(text='.rem')
def rem(channel, nick, message)
    if message[1] == gf and (some hop check here, i know theres one):
        currentgf1 = message[2]
        currentgf2 = message[3]
        return (cc.privmsg(channel, message="Current godfest is set to {0} and {1}!".format(message[3], message[4]))
    elif message[2] == gala and (hop check):
        currentgala = message[2]
        return (cc.privmsg(channel, message="Current gala is set to {0}!".format(message[3]))
    elif (message[2] in pantheons) and (message[3] in pantheons):
        roll = random.choice(#make a list with gala + pantheon and random choose from it)
        #append the roll to wherever the box is stored
        #remove 5 stones from nick
        return (cc.privmsg(channel, message="You rolled a {0}".format(roll))
    elif message[1] in pantheons:
        if message[1] == "current":
            roll = random.choice(#make a list with current gala + pantheon + gfe and random choose from it)
            #append the roll to wherever the box is stored
            #remove 5 stones from nick
            return (cc.privmsg(channel, message="You rolled a {0}".format(roll))
        else:
            roll = random.choice(#make a list with gala + pantheon and random choose from it)
            #append the roll to wherever the box is stored
            #remove 5 stones from nick
            return (cc.privmsg(channel, message="You rolled a {0}".format(roll))
    elif message[1] == None:
        roll = random.choice(#make a list with currentgala + currentgf1-2 set before by some hop + gfe)
        #remove 5 stones from nick
        return (cc.privmsg(channel, message="You rolled a {0}".format(roll))
    else:
        return cc.privmsg(channel, message="I don't understand you")