import collections
import os.path

import requests
from bs4 import BeautifulSoup


Event = collections.namedtuple('Event', ['title', 'members'])

PADXURL = 'http://puzzledragonx.com/'


def fetch(url, parser='html.parser'):
    
    r = requests.get(url)
    
    return BeautifulSoup(r.text, parser)


def parse_rem(soup):
    
    title = soup.find('a', id='rareegg').find_next_sibling('div').h2.string
    members = {id_from_path(path['data-original']) for path in
               soup.find('td', class_='rareegg').find_all('img', title=True)}
    
    return Event(title, members)


def id_from_path(path):
    
    base = os.path.basename(path)
    id, ext = os.path.splitext(base)
    
    return int(id)