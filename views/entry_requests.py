import json
import sqlite3
from models import Entry
from models import Mood

def get_all_entries():
    """This function will return all rows from our SQL table for entries
    """
    with sqlite3.connect('./journal.sqlite3') as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()
        db_cursor.execute("""
        SELECT
            e.id,
            e.concept,
            e.entry,
            e.date,
            e.mood_id,
            m.id,
            m.label
        FROM entries e
        JOIN moods m
            ON m.id = e.mood_id
        """)
        # create an empty list for our entries
        entries = []
        # make data pythonic
        dataset = db_cursor.fetchall()
        # iterate over data and grab each row
        for row in dataset:
            # create a new instance for each row
            entry = Entry(row['id'], row['concept'], row['entry'],
                          row['date'], row['mood_id'])
            mood = Mood(row['id'], row['label'])

            entry.mood = mood.__dict__
            entries.append(entry.__dict__)

    return json.dumps(entries)
