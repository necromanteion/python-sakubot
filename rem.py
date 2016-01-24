import chitchat

#@chitchat.plugin(text='.rem')
async def command(prefix, target, message):

    # parse number of rolls and specified godfests
    # n should default to 1 and have an upper limit
    # n, params = parse(message)

    return (chitchat.reply(roll(params)) for i in range(n))


def roll(params):

    # do stuff

    return # 'You rolled a Sakuya!'
