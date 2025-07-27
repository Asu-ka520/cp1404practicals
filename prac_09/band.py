from musician import Musician

class Band:
    """Class for a band, with a name and members"""

    def __init__(self, name):
        self.name = name
        self.members = []

    def add(self, musician):
        self.members.append(musician)

    def play(self):
        """Returns string of each member playing their instrument."""
        return "\n".join(member.play() for member in self.members)