import sqlite3
import json
from models import Mood

def get_all_moods():
    """This function will return all rows of moods
    """
    with sqlite3.connect('./journal.sqlite3') as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()
        db_cursor.execute("""
        SELECT
            m.id,
            m.label
        FROM moods m
        """)
        # put all our mood instances in a list
        moods = []
        # make our sqlite data pythonic
        dataset = db_cursor.fetchall()
        # iterate over rows of data
        for row in dataset:
            # for every row create a new mood instance
            mood = Mood(row['id'], row['label'])
            # push this instance into our list
            moods.append(mood.__dict__)

    return json.dumps(moods)
