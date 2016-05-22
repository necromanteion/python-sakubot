import collections
import os.path
import sqlite3

from sakubot import sakubot


Card = collections.namedtuple('Card', ['id', 'name', 'rarity', 'cost', 'lv_max',
                                       'feed_xp', 'released', 'sell_price', 'mp',
                                       'attrs'])

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
    
    
def fetch_cursor(query, *params):
    """
    Convenience wrapper around `cursor.execute`.
    
    Equivalent to `connection.cursor().execute(query, params)`.
    """
    
    cursor = sakubot.vars.dbconn.cursor()
    return cursor.execute(query, params)


def fetch_one(query, *params):
    """
    Fetch a single row from a query result.
    
    Equivalent to `connection.cursor().execute(query, params).fetchone()`.
    """
    cursor = fetch_cursor(query, *params)
    
    return cursor.fetchone()
    
    
def fetch_all(query, *params):
    """
    Fetch all rows from a query result.
    
    Equivalent to `connection.cursor().execute(query, params).fetchall()`.
    """
    cursor = fetch_cursor(query, *params)
    
    return cursor.fetchall()
    
    
def name(card_id):
    """Look up only a card's name by its id. Returns the str name or None."""
    
    card = lookup(card_id)
    
    return card.name if card else None


def attributes(card_id):
    """Look up a card's attributes by its id. Returns a list of str attributes."""
    
    query = '''
            SELECT attr.name
            FROM   card_attributes c
                   JOIN attributes attr
                     ON c.attribute = attr.id
            WHERE  c.card = ?
            ORDER  BY c.n;
            '''
    
    attributes = [row[0] for row in fetch_all(query, card_id)]
    
    return attributes


def awakenings(card_id):
    """Look up a card's awakenings by its id. Returns a list of str awakenings."""
    
    query = '''
            SELECT awk.name
            FROM   card_awakenings c
                   JOIN awakenings awk
                     ON c.awakening = awk.id
            WHERE  c.card = ?
            ORDER  BY c.n;
            '''
    
    awakenings = [row[0] for row in fetch_all(query, card_id)]
    
    return awakenings
    

def lookup(card_id):
    """Look up a card by its id. Returns a `Card` object."""
    
    query = 'SELECT * FROM cards WHERE id=?'
    cursor = sakubot.vars.dbconn.cursor()
    
    data = cursor.execute(query, (card_id,)).fetchone()
    
    if data:
        return Card(*data, attributes(card_id))
    
    return None
