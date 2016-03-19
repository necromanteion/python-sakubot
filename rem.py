import chitchat

async def command(prefix, target, message):
    if '-n' in message:
        n = message[2] 
        for i in n
            databess.removeStones(target, n)
        return (rem(prefix, target, message) for i in range(n))
    else:  
        databess.removeStones(target, 1)
        return rem(prefix, target, message)

pantheons=[greek1, greek2, japanese1, japanese2, indian1, indian2, egyptian1, egyptian2, hero, threekingdoms, samurai, constellation1, constellation2, chinese, archangel, archdemon]

def rem(channel, nick, message)
    if message[1] == gf and (nick in cmds.nicklist):
        currentgf1 = message[2]
        currentgf2 = message[3]
        return cc.privmsg(channel, message="Current godfest is set to {0} and {1}!".format(message[3], message[4])
    elif message[2] == gala and (nick in cmds.nicklist):
        currentgala = message[2]
        return cc.privmsg(channel, message="Current gala is set to {0}!".format(message[3])
    elif (message[2] in pantheons) and (message[3] in pantheons):
        roll = random.choice(#make a list with gala + pantheon and random choose from it)
            databess.addbox(nick, roll)
        return cc.privmsg(channel, message="You rolled a {0}".format(roll)
    elif message[1] in pantheons:
        if message[1] == "current":
            roll = random.choice(#make a list with current gala + pantheon + gfe and random choose from it)
            databess.addbox(nick, roll)
            return cc.privmsg(channel, message="You rolled a {0}".format(roll)
        else:
            roll = random.choice(#make a list with gala + pantheon and random choose from it)
            databess.addbox(nick, roll)
            return cc.privmsg(channel, message="You rolled a {0}".format(roll)
    elif message[1] == None:
        roll = random.choice(#make a list with currentgala + currentgf1-2 set before by some hop + gfe)
        return cc.privmsg(channel, message="You rolled a {0}".format(roll)
    else:
        return cc.privmsg(channel, message="I don't understand you.")
