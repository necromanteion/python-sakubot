from .structures import Event, MutuallyExclusiveEvent
from .utils import multmerge

GALA_RATE = 2
FOUR_STAR_RATE = 6
FIVE_STAR_RATE = 3
SIX_STAR_RATE = 1

DEFAULT = Event(
    title=None,
    members=multmerge(
        # 4*
        dict.fromkeys([111, 112, 114, 116, 118, 120, 352, 354, 356, 358, 360, 414,
                       417, 420, 423, 426, 486, 488, 1120, 1122, 1124, 1126, 1128,
                       1349, 1351, 1353, 1412, 1414, 1416, 1418, 1420, 1502, 1504,
                       1506, 1896, 1898], FOUR_STAR_RATE),
        # 5*
        dict.fromkeys([113, 115, 117, 119, 121, 122, 124, 126, 128, 130, 132, 134,
                       136, 138, 140, 236, 238, 240, 242, 244, 353, 355, 357, 359,
                       361, 368, 370, 372, 374, 376, 378, 380, 382, 384, 386, 415,
                       418, 421, 424, 427, 490, 492, 494, 496, 498, 555, 557, 559,
                       561, 563, 567, 569, 571, 573, 575, 620, 622, 624, 626, 628,
                       630, 632, 634, 636, 638, 745, 747, 749, 751, 753, 799, 801,
                       803, 805, 807, 1065, 1067, 1069, 1071, 1073, 1076, 1078, 1080,
                       1082, 1084, 1121, 1123, 1125, 1127, 1129, 1130, 1231, 1233,
                       1235, 1237, 1239, 1241, 1330, 1332, 1334, 1336, 1338, 1350,
                       1352, 1354, 1355, 1357, 1359, 1372, 1413, 1415, 1417, 1419,
                       1421, 1503, 1505, 1507, 1614, 1616, 1618, 1620, 1622, 1624,
                       1626, 1649, 1651, 1653, 1655, 1657, 1659, 1661, 1663, 1665,
                       1667, 1704, 1706, 1755, 1757, 1826, 1828, 1830, 1832, 1834,
                       1881, 1882, 1883, 1884, 1885, 1897, 1899, 2093, 2095, 2097,
                       2099, 2101, 2185, 2186, 2187, 2188, 2189, 2190, 2191, 2192,
                       2193, 2194, 2264, 2266, 2268, 2270, 2272, 2415, 2417, 2419,
                       2421, 2423, 2552, 2554, 2556, 2558, 2560], FIVE_STAR_RATE),
        # 6*
        dict.fromkeys([379, 381, 383, 385, 387, 556, 558, 560, 562, 564, 1131, 1243,
                       1356, 1358, 1374], SIX_STAR_RATE)
    ),
    pattern=None
)

### GALAS ###

FIRE_GALA = Event(
    title='Gala of Flame',
    members=dict.fromkeys([112, 113, 122, 132, 236, 352, 353, 368, 378, 379, 414, 415,
                           490, 555, 556, 567, 620, 630, 745, 799, 1065, 1076, 1120,
                           1121, 1231, 1243, 1330, 1349, 1350, 1355, 1356, 1412, 1413,
                           1502, 1503, 1614, 1649, 1659, 1706, 1826, 1881, 2093, 2185,
                           2190, 2264, 2415, 2552], GALA_RATE),
    pattern=r'^f(ire)?$'
)

WATER_GALA = Event(
    title='Gala of Tides',
    members=dict.fromkeys([114, 115, 124, 134, 238, 354, 355, 370, 380, 381, 417, 418,
                           488, 492, 557, 558, 569, 622, 632, 747, 801, 1067, 1078,
                           1122, 1123, 1233, 1332, 1414, 1415, 1504, 1505, 1616, 1651,
                           1661, 1828, 1882, 2095, 2186, 2191, 2266, 2417, 2554], GALA_RATE),
    pattern=r'^w[at]+(er)?$'
)

WOOD_GALA = Event(
    title='Forest Gala',
    members=dict.fromkeys([116, 117, 126, 136, 240, 356, 357, 372, 382, 383, 420, 421,
                           494, 559, 560, 571, 624, 634, 749, 803, 1069, 1080, 1124,
                           1125, 1130, 1131, 1235, 1241, 1334, 1351, 1352, 1372, 1416,
                           1417, 1618, 1653, 1663, 1704, 1830, 1883, 1896, 1897, 2097,
                           2187, 2192, 2268, 2419, 2556], GALA_RATE),
    pattern=r'^wo+d?$'
)

LIGHT_GALA = Event(
    title="Heaven's Gala",
    members=dict.fromkeys([118, 119, 128, 138, 242, 358, 359, 374, 384, 385, 423, 424,
                           496, 561, 562, 573, 626, 636, 751, 805, 1071, 1082, 1126,
                           1127, 1237, 1336, 1353, 1354, 1359, 1374, 1418, 1419, 1506,
                           1507, 1620, 1624, 1655, 1665, 1755, 1832, 1884, 2099, 2188,
                           2193, 2270, 2421, 2558], GALA_RATE),
    pattern=r'^li[gh]*t$'
)

DARK_GALA = Event(
    title='Midnight Gala',
    members=dict.fromkeys([111, 120, 121, 130, 140, 244, 360, 361, 376, 386, 387, 426,
                           427, 486, 498, 563, 564, 575, 628, 638, 753, 807, 1073,
                           1084, 1128, 1129, 1239, 1338, 1357, 1358, 1420, 1421, 1622,
                           1626, 1657, 1667, 1757, 1834, 1885, 1898, 1899, 2101, 2189,
                           2194, 2272, 2423, 2560], GALA_RATE),
    pattern=r'^da?r?k'
)

### PANTHEONS ###

GRECO = Event(
    title='Greco-Roman',
    members=multmerge(
        dict.fromkeys([122, 124, 126, 128, 130], FIVE_STAR_RATE),
        dict.fromkeys([123, 125, 127, 129, 131], SIX_STAR_RATE)
    ),
    pattern=r'(g(re+[ck]o?)?|r(om[ae]n?)?)$'
)

JAPANESE = Event(
    title='Japanase',
    members=multmerge(
        dict.fromkeys([132, 134, 136, 138, 140], FIVE_STAR_RATE),
        dict.fromkeys([133, 135, 137, 139, 141], SIX_STAR_RATE)
    ),
    pattern=r'^ja?p(an(ese)?)?$'
)

INDIAN = Event(
    title='Indian',
    members=multmerge(
        dict.fromkeys([236, 238, 240, 242, 244], FIVE_STAR_RATE),
        dict.fromkeys([237, 239, 241, 243, 245], SIX_STAR_RATE)
    ),
    pattern=r'^in(d(ian)?)?$'
)

NORSE = Event(
    title='Norse',
    members=multmerge(
        dict.fromkeys([368, 370, 372, 374, 376], FIVE_STAR_RATE),
        dict.fromkeys([369, 371, 373, 375, 377], SIX_STAR_RATE)
    ),
    pattern=r'^n(orse)?$'
)

EGYPTIAN = Event(
    title='Egyptian',
    members=multmerge(
        dict.fromkeys([490, 492, 494, 496, 498], FIVE_STAR_RATE),
        dict.fromkeys([491, 493, 495, 497, 499], SIX_STAR_RATE)
    ),
    pattern=r'^e(gypt(ian)?)?$'
)

GREEK = Event(
    title='Greek',
    members=multmerge(
        dict.fromkeys([567, 569, 571, 573, 575], FIVE_STAR_RATE),
        dict.fromkeys([568, 570, 572, 574, 576], SIX_STAR_RATE)
    ),
    pattern=r'^g(re+ek)?2(\.0)?$'
)

ARCHANGEL = Event(
    title='Archangels',
    members=multmerge(
        dict.fromkeys([620, 622, 624, 626, 628], FIVE_STAR_RATE),
        dict.fromkeys([621, 623, 625, 627, 629], SIX_STAR_RATE)
    ),
    pattern=r'^a(rch)?a(ngels?)?$'
)

ARCHDEMON = Event(
    title='Archdemons',
    members=multmerge(
        dict.fromkeys([630, 632, 634, 636, 638], FIVE_STAR_RATE),
        dict.fromkeys([631, 633, 635, 637, 639], SIX_STAR_RATE)
    ),
    pattern=r'^a(rch)?d(emons?)?$'
)

CHINESE = Event(
    title='Chinese',
    members=multmerge(
        dict.fromkeys([745, 747, 749, 751, 753], FIVE_STAR_RATE),
        dict.fromkeys([746, 748, 750, 752, 754], SIX_STAR_RATE)
    ),
    pattern=r'^ch(in(a|ese)?)?$'
)

JAPANESE2 = Event(
    title='Japanese 2',
    members=multmerge(
        dict.fromkeys([799, 801, 803, 805, 807], FIVE_STAR_RATE),
        dict.fromkeys([800, 802, 804, 806, 808], SIX_STAR_RATE)
    ),
    pattern=r'^ja?p(an(ese)?)?2(\.0)?$'
)

HEROES = Event(
    title='Heroes',
    members=multmerge(
        dict.fromkeys([1065, 1067, 1069, 1071, 1073], FIVE_STAR_RATE),
        dict.fromkeys([1066, 1068, 1070, 1072, 1074], SIX_STAR_RATE)
    ),
    pattern=r'^h(eroe?s?)?$'
)

THREE_KINGDOMS = Event(
    title='Three Kingdoms',
    members=multmerge(
        dict.fromkeys([1231, 1232, 1233, 1234, 1235, 1236, 1237, 1238, 1239, 1240], FIVE_STAR_RATE),
        dict.fromkeys([1231, 1232, 1233, 1234, 1235, 1236, 1237, 1238, 1239, 1240], SIX_STAR_RATE)
    ),
    pattern=r'^3?k(ing(doms?)?)?$'
)

INDIAN2 = Event(
    title='Indian 2',
    members=multmerge(
        dict.fromkeys([1330, 1332, 1334, 1336, 1338], FIVE_STAR_RATE),
        dict.fromkeys([1331, 1333, 1335, 1337, 1339], SIX_STAR_RATE)
    ),
    pattern=r'^i(n(d(ian)?)?)?2(\.0)?$'
)

EGYPTIAN2 = Event(
    title='Egyptian 2',
    members=multmerge(
        dict.fromkeys([1659, 1661, 1663, 1665, 1667], FIVE_STAR_RATE),
        dict.fromkeys([1660, 1662, 1664, 1666, 1668], SIX_STAR_RATE)
    ),
    pattern=r'^e(g(ypt(ian)?)?)?2(\.0)?$'
)

ANGELS = Event(
    title='Angels',
    members=multmerge(
        dict.fromkeys([1826, 1828, 1830, 1832, 1834], FIVE_STAR_RATE),
        dict.fromkeys([1827, 1829, 1831, 1833, 1835], SIX_STAR_RATE)
    ),
    pattern=r'^a(ngels?)?$'
)

SENGOKU = Event(
    title='Sengoku',
    members=multmerge(
        dict.fromkeys([2264, 2266, 2268, 2270, 2272], FIVE_STAR_RATE),
        dict.fromkeys([2265, 2267, 2269, 2271, 2273], SIX_STAR_RATE)
    ),
    pattern=r'^s(en(goku)?|am(urai)?)?$'
)

CONSTELLATIONS = Event(
    title='Constellations',
    members=multmerge(
        dict.fromkeys([2415, 2417, 2419, 2421, 2423], FIVE_STAR_RATE),
        dict.fromkeys([2416, 2418, 2420, 2422, 2424], SIX_STAR_RATE)
    ),
    pattern=r'^c(on(st(ell*(ations?)?)?)?)?$'
)

CONSTELLATIONS2 = Event(
    title='Constellations 2',
    members=multmerge(
        dict.fromkeys([2552, 2554, 2556, 2558, 2560], FIVE_STAR_RATE),
        dict.fromkeys([2553, 2555, 2557, 2559, 2561], SIX_STAR_RATE)
    ),
    pattern=r'^c(on(st(ell*(ations?)?)?)?)?2(\.0)?$'
)

### COLLABS ###

DC_UNIVERSE = MutuallyExclusiveEvent(
    title='DC Universe',
    members=multmerge(
        dict.fromkeys([1679, 1681, 1683, 1685, 1687], FOUR_STAR_RATE),
        dict.fromkeys([1675, 1677, 2826], FIVE_STAR_RATE)
    ),
    pattern=r'((bat|super)(man)?|dc)'
)

EVENTS = [FIRE_GALA, WATER_GALA, WOOD_GALA, LIGHT_GALA, DARK_GALA,
          GRECO, JAPANESE, INDIAN, NORSE, EGYPTIAN, GREEK,
          ARCHANGEL, ARCHDEMON, CHINESE, JAPANESE2, HEROES,
          THREE_KINGDOMS, INDIAN2, EGYPTIAN2, ANGELS, SENGOKU,
          CONSTELLATIONS, CONSTELLATIONS2,
          DC_UNIVERSE]