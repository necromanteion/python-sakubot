"""
hentapi: A Sakubot plugin for ex/e-hentai links.

TODO: rewrite using urllib2 instead of requests
"""

import chitchat as cc
import urllib.parse
import requests

from sakubot import sakubot

API = 'http://g.e-hentai.org/api.php'
SKIPPED = 'artist', 'group', 'language'


def valid_gallery(url):
    parsed = urllib.parse.urlparse(url)
    
    if parsed.netloc.lower() not in ('exhentai.org', 'g.e-hentai.org'):
        return False
    
    try:
        _, flag, gid, token, *_ = parsed.path.split('/')
        assert flag == 'g'
        
    except (AssertionError, ValueError):
        return False
    
    return gid, token


def format_tags(tags, skip=None):
    
    skip = skip or []
    
    parsed = []
    for tag in tags:
        
        try:
            category, t = tag.split(':', maxsplit=1)
            
        except ValueError:
            category, t = None, tag
        
        if category not in skip:
            formatted = '{0} ({1[0]})'.format(t, category or '?')
            parsed.append(formatted)
        
    return 'tags: ' + ', '.join(sorted(parsed))


@sakubot.on('PRIVMSG', text=valid_gallery)
def plugin(prefix, target, message):
    
    gid, token = valid_gallery(message)
    req = dict(method='gdata', gidlist=[[gid, token]], namespace=1)
    
    resp = requests.post(API, json=req)
    resp.encoding = 'UTF-8'
    
    doujin = resp.json()['gmetadata'][0]
    
    if 'error' in doujin:
        return None
    
    lines = [
        '"{0[title]}" (★ {0[rating]})'.format(doujin),
        format_tags(doujin['tags'], skip=SKIPPED)
    ]
    
    return [cc.privmsg(target, line) for line in lines]
