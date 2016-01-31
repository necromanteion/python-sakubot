import collections
import os.path

import requests
from bs4 import BeautifulSoup


PADXURL = 'http://puzzledragonx.com/'


class Event(collections.namedtuple('Event', ['title', 'members'])):
    
    def __add__(self, other):
        
        if isinstance(other, type(self)):
            title = ', '.join([self.title, other.title])
            members = self.members | other.members
            
            return Event(title, members)
        
        return super().__add__(other)


def urlsoup(url, parser='html.parser'):
    
    r = requests.get(url)
    
    return BeautifulSoup(r.text, parser)


def parse_godfest(soup):
    """Searches a soup for the current REM godfest"""
    
    title_links = soup.find('td', class_='godfeslist').find_all('a', class_='bold')
    title = ', '.join(link.string for link in title_links)
    
    table = soup.find('td', class_='godfeslist').parent.find_next_sibling('table')
    members = {id_from_url(img['data-original']) for img in table.find('img', title=True)}
    
    return Event(title, members)


def parse_gala(soup):
    """Searches a soup for the current REM gala."""
    
    title = soup.find('a', id='rareegg').find_next_sibling('div').h2.string
    members = {id_from_url(img['data-original']) for img in
               soup.find('td', class_='rareegg').find_all('img', title=True)}
    
    return Event(title, members)


def parse_rem(soup):
    """Searches a soup for current REM events."""
    
    godfest = parse_godfest(soup)
    gala = parse_gala(soup)
    
    return godfest + gala


def id_from_url(url):
    """Parses the monster id from its resource path and returns as an integer."""
    
    base = os.path.basename(url)
    id, ext = os.path.splitext(base)
    
    return int(id)


if __name__ == '__main__':
    
    soup = urlsoup(PADXURL)
    
    print(parse_rem(soup))