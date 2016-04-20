import collections
import os.path
import sqlite3

from sakubot import sakubot


Card = collections.namedtuple('Card', ['id', 'name', 'rarity', 'cost', 'lv_max',
                                       'feed_xp', 'released', 'sell_price', 'mp'])

PATH = os.path.join(os.path.dirname(__file__), 'pad.db')

@sakubot.on('CONNECTED')
def initialize(*args):
    """Initialize connection to database."""
    sakubot.vars.dbconn = sqlite3.connect(PATH)

    
@sakubot.on('DISCONNECTED')
def close(*args):
    """Close the database connection."""
    
    try:
        sakubot.vars.dbconn.close()
        del sakubot.vars.dbconn
    
    # already closed or nonexistent
    except AttributeError:
        pass
    
    
def name(card_id):
    """Look up only a card's name by its id. Returns the str name or None."""
    
    card = lookup(card_id)
    
    return card.name if card else None
    

def lookup(card_id):
    """Look up a card by its id. Returns a `Card` object."""
    
    query = 'SELECT * FROM cards WHERE id=?'
    cursor = sakubot.vars.dbconn.cursor()
    
    data = cursor.execute(query, (card_id,)).fetchone()
    
    if data:
        return Card(*data)
    
    return None