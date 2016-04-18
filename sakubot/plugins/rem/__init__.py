import chitchat as cc
from sakubot import sakubot

from .parsing import first_int, matches
from .structures import ErrorRaisingArgumentParser, Event
from .utils import combine, percent


EVENTS = [
    Event(None, dict.fromkeys([111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 124, 126, 128, 128, 130, 132, 134, 136, 138, 138, 140, 236, 238, 240, 242, 242, 244, 352, 353, 354, 355, 356, 357, 358, 359, 359, 360, 361, 368, 370, 372, 374, 374, 376, 378, 379, 380, 381, 382, 383, 384, 384, 385, 386, 387, 414, 415, 417, 418, 420, 421, 423, 424, 424, 426, 427, 486, 488, 490, 492, 494, 496, 496, 498, 555, 556, 557, 558, 559, 560, 561, 561, 562, 563, 564, 567, 569, 571, 573, 573, 575, 620, 622, 624, 626, 626, 628, 630, 632, 634, 636, 636, 638, 745, 747, 749, 751, 751, 753, 799, 801, 803, 805, 805, 807, 1065, 1067, 1069, 1071, 1071, 1073, 1076, 1078, 1080, 1082, 1082, 1084, 1120, 1121, 1122, 1123, 1124, 1125, 1126, 1127, 1127, 1128, 1129, 1130, 1131, 1231, 1233, 1235, 1237, 1237, 1239, 1241, 1243, 1330, 1332, 1334, 1336, 1336, 1338, 1349, 1350, 1351, 1352, 1353, 1354, 1354, 1355, 1356, 1357, 1358, 1359, 1372, 1374, 1412, 1413, 1414, 1415, 1416, 1417, 1418, 1419, 1419, 1420, 1421, 1502, 1503, 1504, 1505, 1506, 1506, 1507, 1507, 1614, 1616, 1618, 1620, 1620, 1622, 1624, 1624, 1626, 1649, 1651, 1653, 1655, 1655, 1657, 1659, 1661, 1663, 1665, 1665, 1667, 1704, 1706, 1755, 1755, 1757, 1826, 1828, 1830, 1832, 1832, 1834, 1881, 1882, 1883, 1884, 1884, 1885, 1896, 1897, 1898, 1899, 2093, 2095, 2097, 2099, 2099, 2101, 2185, 2186, 2187, 2188, 2188, 2189, 2190, 2191, 2192, 2193, 2193, 2194, 2264, 2266, 2268, 2270, 2270, 2272, 2415, 2417, 2419, 2421, 2421, 2423, 2552, 2554, 2556, 2558, 2558, 2560], 1.0), r'.*'),
    Event('Gala of Flame', dict.fromkeys([112, 113, 122, 132, 236, 352, 353, 368, 378, 379, 414, 415, 490, 555, 556, 567, 620, 630, 745, 799, 1065, 1076, 1120, 1121, 1231, 1243, 1330, 1349, 1350, 1355, 1356, 1412, 1413, 1502, 1503, 1614, 1649, 1659, 1706, 1826, 1881, 2093, 2185, 2190, 2264, 2415, 2552], 2.0), r'^f'),
    Event('Gala of Tides', dict.fromkeys([114, 115, 124, 134, 238, 354, 355, 370, 380, 381, 417, 418, 488, 492, 557, 558, 569, 622, 632, 747, 801, 1067, 1078, 1122, 1123, 1233, 1332, 1414, 1415, 1504, 1505, 1616, 1651, 1661, 1828, 1882, 2095, 2186, 2191, 2266, 2417, 2554], 2.0), r'^wa?t'),
    Event('Forest Gala', dict.fromkeys([116, 117, 126, 136, 240, 356, 357, 372, 382, 383, 420, 421, 494, 559, 560, 571, 624, 634, 749, 803, 1069, 1080, 1124, 1125, 1130, 1131, 1235, 1241, 1334, 1351, 1352, 1372, 1416, 1417, 1618, 1653, 1663, 1704, 1830, 1883, 1896, 1897, 2097, 2187, 2192, 2268, 2419, 2556], 2.0), r'^wo+d'),
    Event("Heaven's Gala", dict.fromkeys([118, 119, 128, 138, 242, 358, 359, 374, 384, 385, 423, 424, 496, 561, 562, 573, 626, 636, 751, 805, 1071, 1082, 1126, 1127, 1237, 1336, 1353, 1354, 1359, 1374, 1418, 1419, 1506, 1507, 1620, 1624, 1655, 1665, 1755, 1832, 1884, 2099, 2188, 2193, 2270, 2421, 2558], 2.0), r'^li[gh]*t'),
    Event('Midnight Gala', dict.fromkeys([111, 120, 121, 130, 140, 244, 360, 361, 376, 386, 387, 426, 427, 486, 498, 563, 564, 575, 628, 638, 753, 807, 1073, 1084, 1128, 1129, 1239, 1338, 1357, 1358, 1420, 1421, 1622, 1626, 1657, 1667, 1757, 1834, 1885, 1898, 1899, 2101, 2189, 2194, 2272, 2423, 2560], 2.0), r'^da?r?k'),
    Event('Greco-Roman', dict.fromkeys([122, 123, 124, 125, 126, 127, 128, 129, 130, 131], 3.0), r'(g(re+[ck]o?)?|r(om[ae]n?)?)$'),
    Event('Japanese', dict.fromkeys([132, 133, 134, 135, 136, 137, 138, 139, 140, 141], 3.0), r'^ja?p(an(ese)?)?$'),
    Event('Indian', dict.fromkeys([236, 237, 238, 239, 240, 241, 242, 243, 244, 245], 3.0), r'^in(d(ian)?)?$'),
    Event('Norse', dict.fromkeys([368, 369, 370, 371, 372, 373, 374, 375, 376, 377], 3.0), r'^n(orse)?$'),
    Event('Egyptian', dict.fromkeys([490, 491, 492, 493, 494, 495, 496, 497, 498, 499], 3.0), r'^e(gypt(ian)?)?$'),
    Event('Greek', dict.fromkeys([567, 568, 569, 570, 571, 572, 573, 574, 575, 576], 3.0), r'^g(re+ek)?2(\\.0)?$'),
    Event('Archangels', dict.fromkeys([620, 621, 622, 623, 624, 625, 626, 627, 628, 629], 3.0), r'^a(rch)?a(ngels?)?$'),
    Event('Archdemons', dict.fromkeys([630, 631, 632, 633, 634, 635, 636, 637, 638, 639], 3.0), r'^a(rch)?d(emons?)?$'),
    Event('Chinese', dict.fromkeys([745, 746, 747, 748, 749, 750, 751, 752, 753, 754], 3.0), r'^ch(in(a|ese)?)?$'),
    Event('Japanese 2', dict.fromkeys([799, 800, 801, 802, 803, 804, 805, 806, 807, 808], 3.0), r'^ja?p(an(ese)?)?2(\\.0)?$'),
    Event('Heroes', dict.fromkeys([1065, 1066, 1067, 1068, 1069, 1070, 1071, 1072, 1073, 1074], 3.0), r'^h(eroe?s?)?$'),
    Event('Three Kingdoms', dict.fromkeys([1231, 1232, 1233, 1234, 1235, 1236, 1237, 1238, 1239, 1240], 3.0), r'^3?k(ing(doms?)?)?$'),
    Event('Indian 2', dict.fromkeys([1330, 1331, 1332, 1333, 1334, 1335, 1336, 1337, 1338, 1339], 3.0), r'^i(n(d(ian)?)?)?2(\\.0)?$'),
    Event('Egyptian 2', dict.fromkeys([1659, 1660, 1661, 1662, 1663, 1664, 1665, 1666, 1667, 1668], 3.0), r'^e(g(ypt(ian)?)?)?2(\\.0)?$'),
    Event('Angels', dict.fromkeys([1826, 1827, 1828, 1829, 1830, 1831, 1832, 1833, 1834, 1835], 3.0), r'^a(ngels?)?$'),
    Event('Sengoku', dict.fromkeys([2264, 2265, 2266, 2267, 2268, 2269, 2270, 2271, 2272, 2273], 3.0), r'^s(en(goku)?|am(urai)?)?$'),
    Event('Constellations', dict.fromkeys([2415, 2416, 2417, 2418, 2419, 2420, 2421, 2422, 2423, 2424], 3.0), r'^c(on(st(ell*(ations?)?)?)?)?$'),
    Event('Constellations 2', dict.fromkeys([2552, 2553, 2554, 2555, 2556, 2557, 2558, 2559, 2560, 2561], 3.0), r'^c(on(st(ell*(ations?)?)?)?)?2(\\.0)?$')
]

parser = ErrorRaisingArgumentParser(prog='.rem', add_help=False)
parser.add_argument('-n', default=1, type=int)

group = parser.add_mutually_exclusive_group(required=False)
group.add_argument('-c', '--chance', metavar='ID', type=int)
group.add_argument('-u', '--until', metavar='ID', type=int)


@sakubot.on('PRIVMSG', text='.rem')
def rem(prefix, target, message):
    
    try:
        flags, args = parser.parse_known_args(message.split())
    
    except ValueError:
        return usage(prefix, target)
    
    # build weighted rem from unparsed args
    rem = combine(combine(matches(arg, EVENTS)) for arg in args)
    
    if flags.chance:
        return chance(prefix, target, event=rem, card=flags.chance, n=flags.n)
    
    elif flags.until:
        return until(prefix, target, event=rem, card=flags.until)
    
    return roll(prefix, target, event=rem, n=min(flags.n, 5))


def usage(prefix, target):
    """
    Return a generic usage message on error.
    """
    
    line = '{0.nick} no baka! Use it like this: {1} [event [event ...]]'
    # remove preceding 'usage: ' and concluding newline from parser's usage message
    line = line.format(prefix, ' '.join(parser.format_usage().strip().split()[1:]))
    
    return cc.privmsg(target, line)
    

def chance(prefix, target, event, card, n=1):
    """
    Calculate the percent chance of rolling `card` in `n` rolls of `event` and return a
    privmsg of the results.
    
    """
    
    chance = event.chance(card, n)
    
    line = 'You have a {0} chance of rolling #{1} in {2} rolls of the {3.padded_title}REM.'
    line = line.format(percent(chance), card, n, event)
    
    return cc.privmsg(target, line)


def until(prefix, target, event, card):
    """
    Roll in `event` until `card` is found and return a privmsg of the number of rolls
    necessary.
    
    """
    
    try:
        n = event.roll_until(card)
    
    except ValueError:
        line = ("Onii-chan your fat, greasy fingers must've made a typo, #{0} isn't in "
                'the {1.padded_title}REM!')
        line = line.format(card, event)
        return cc.privmsg(target, line)
    
    if n:
        line = 'It took me {0} rolls of the {1.padded_title}REM to roll #{2}!'
        line = line.format(n, event, card)
    
    else:
        line = "Sorry onii-chan, looks like you don't have enough stones for that."
        
    return cc.privmsg(target, line)


def roll(prefix, target, event, n=1):
    """Roll `n` times, yielding each result as an individual privmsg."""
        
    for card in event.roll(n):
        line = "{0.nick}-nii's {1.padded_title}REM roll: #{2}!"
        line = line.format(prefix, event, card)
        yield cc.privmsg(target, line)