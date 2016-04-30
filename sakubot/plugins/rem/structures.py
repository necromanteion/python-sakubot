import argparse
import bisect
import collections
import itertools
import random
import re

from . import utils


class Event(collections.abc.MutableMapping):
    
    
    def __init__(self, title, members, pattern=None):
        self.title = title
        self.members = members
        self.pattern = pattern
        
    
    @property
    def title(self):
        title = ', '.join(filter(None, self._title))
            
        return title
    
    
    @title.setter
    def title(self, value):
        self._title = [value] if isinstance(value, (str, type(None))) else list(value)
        
        
    @property
    def formatted_title(self):
        title = self.title + ' REM'
        
        return title.strip()
    
    
    @property
    def pattern(self):
        return self._pattern
    
    
    @pattern.setter
    def pattern(self, value):
        self._pattern = re.compile(value, flags=re.I) if value else None
        
        
    @pattern.deleter
    def pattern(self):
        del self._pattern
        
        
    @property
    def match(self):
        try:
            return self._pattern.match
        
        except AttributeError:
            return None
        
    
    def chance(self, card_id, n=1):
        """
        Calculate the chance of rolling card `card_id` in `n` rolls.
        
        args:
            card_id (int): ID of the card to calculate the chance of rolling
            n (int): number of rolls, defaults to 1
        
        returns:
            float chance between 0 and 1, inclusive
        """
        
        weight = self.get(card_id, 0)
        total = sum(self.values())
        
        # chance of rolling = 1 - chance of not rolling
        return 1 - (1 - weight / total) ** n
        
        
    def roll(self, n=1):
        """
        Roll `n` random cards from the event's weighted population.
        
        args:
            n (int): number of times to roll
        
        yields:
            `n` int card ids
            
        raises:
            TypeError if `n` is not an integer
        """
        
        choices, weights = zip(*self.items())
        cumdist = list(itertools.accumulate(weights))
        
        for i in range(n):
            x = random.random() * cumdist[-1]
            i = bisect.bisect(cumdist, x)
            
            yield choices[i]
    
    
    def roll_until(self, card_id, max_rolls=5000):
        """
        Call `self.roll` until card `card_id` is rolled, and return the number of rolls
        required.
        
        args:
            card_id (int): ID of the card to roll for
            max_rolls (int): maximum number of iterations to attempt, defaults to 5000
        
        returns:
            int number of iterations until `card_id` is rolled, or False to indicate the
            card was not rolled in `max_rolls` rolls
            
        raises:
            ValueError if `card_id` is not featured in this event
        """
        
        if card_id not in self:
            raise ValueError('card #{0!r} is not featured in this event'.format(card_id))
        
        rollgen = self.roll(max_rolls)
        
        for i, roll in enumerate(rollgen, start=1):
            
            if roll == card_id:
                return i
        
        return False
    
    
    def __getitem__(self, key):
        return self.members[key]
    
    
    def __setitem__(self, key, value):
        self.members[key] = value
    
    
    def __delitem__(self, key):
        del self.members[key]
        
        
    def __iter__(self):
        return iter(self.members.keys())
    
    
    def __len__(self):
        return len(self.members)
        
        
    def __add__(self, other):
        
        # can't use isinstance(other, Event) because MutuallyExclusiveEvent instances
        # are considered Event instances due to inheritance
        if type(other) == type(self):
            
            titles = self.title, other.title            
            members = utils.multmerge(self, other)
            
            return Event(titles, members)
        
        return NotImplemented
    
    
    def __radd__(self, other):
        return self + other
        
        
    def __repr__(self):
        rep = '{0.__class__.__name__}(title={0.title!r}, members={0.members!r})'
        return rep.format(self)
    
    
class MutuallyExclusiveEvent(Event):
    
    
    def __add__(self, other):
        
        if isinstance(other, Event):
            return self
            
        return NotImplemented
    
    
class ErrorRaisingArgumentParser(argparse.ArgumentParser):
    """
    `argparse.ArgumentParser` subclass that overrides the behavior on error to raise the
    error instead of exiting.
    
    """
    
    def error(self, message):
        
        if 'value' in message:
            raise ValueError(message)
        
    def format_usage(self):
        # remove preceding 'usage: ' and concluding newline
        usage = super().format_usage().strip().split()[1:]
        
        return ' '.join(usage)