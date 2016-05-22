import collections
import functools
import operator
import math


def colorize(attribute):
    """
    Attribute • [Fire, Water, Wood, Light, Dark]:
    4 12 3 8 6
    
    Rarity ⭐  or 🌟[1, 2, 3, 4, 5+]:
    9 8 11 15 7
    """
    pass



def percent(n, precision=0):
    """
    Converts `n` to an appropriately-precise percentage.
    """
    
    # 'or 1' prevents a domain error if n == 0 (i.e., 0%)
    places = precision - math.floor(math.log10(abs(n) or 1))
    return '{0:.{1}%}'.format(n, places)
    

def multmerge(*dicts):
    """
    Multiplicatively merge dictionaries.
    
    >>> d = dict(a=2), dict(a=3, b=2)
    >>> multmerge(*d)
    {'a': 6, 'b': 2}
    """
    
    intermediate = collections.defaultdict(lambda: 1)
    
    for d in dicts:
        
        for key, value in d.items():
            intermediate[key] *= value
            
    return dict(intermediate)


def combine(*args, func=operator.add, initializer=None):
    """
    Like `sum` but doesn't start with 0; good for classes with custom __add__ behavior.
    
    """
    
    if len(args) == 1:
        args = args[0]
    
    # damn thing only takes positional arguments
    if initializer is None:
        return functools.reduce(func, args)
    
    return functools.reduce(func, args, initializer)