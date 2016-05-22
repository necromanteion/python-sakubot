import ssl
import types
from . import sakubot

context = ssl.create_default_context()

sakubot.vars = types.SimpleNamespace()
sakubot.run(host='irc.rizon.net', port=6697, ssl=context)
