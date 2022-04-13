class Entry():
    """This class creates an instance of a new entry
    """
    def __init__(self, id, concept, entry, date, mood_id):
        self.id = id
        self.concept = concept
        self.entry = entry
        self.date = date
        self.mood_id = mood_id
        self.mood = None

new_entry = Entry(1, "Convo", "Wassup", "4/14/22", 3)
