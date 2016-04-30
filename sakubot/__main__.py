import ssl
import types
from . import sakubot

sakubot.vars = types.SimpleNamespace()
sakubot.run(host='irc.rizon.net', port=6697, ssl=ssl.get_default_context())
