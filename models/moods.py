class Mood():
    """This class creates a instance of a new mood
    """
    def __init__(self, id, label):
        self.id = id
        self.label = label

new_mood = Mood(1, "good")
