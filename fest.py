import collections
import os.path

import requests
from lxml import html


Event = collections.namedtuple('Event', ['title', 'members'])

PADXURL = 'http://puzzledragonx.com/'
REMTITLE = '//table[@id="event"]//a[@id="rareegg"]/../div/h2'
# rem icon src is spacer.gif until loaded, must use data-original attribute
REMMEMBERS = '//td[@class="rareegg"]//td[@class="peticon"]/a/img/@data-original'


def fetch(url):
    
    r = requests.get(url)
    
    return html.document_fromstring(r.text)


def parse_rem(document):
    
    title = document.xpath(REMTITLE)[0].text
    members = {id_from_path(path) for path in document.xpath(REMMEMBERS)}
    
    return Event(title, members)


def id_from_path(path):
    
    base = os.path.basename(path)
    id, ext = os.path.splitext(base)
    
    return int(id)


if __name__ == '__main__':
    doc = fetch(PADXURL)
    event = parse_rem(doc)
    
    print(event)