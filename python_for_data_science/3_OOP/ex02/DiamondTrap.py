from S1E7 import Baratheon, Lannister


class King(Baratheon, Lannister):
    """
    King class representing Joffrey Baratheon,
        inheriting from both Baratheon and Lannister.
    This demonstrates the diamond problem in multiple inheritance.
    """
    def __init__(self, name):
        """Initialize the King with given name"""
        super().__init__(name)

    def set_eyes(self, color):
        """Set the eye color"""
        self.eyes = color

    def get_eyes(self):
        """Get the eye color"""
        return self.eyes

    def set_hairs(self, color):
        """Set the hair color"""
        self.hairs = color

    def get_hairs(self):
        """Get the hair color"""
        return self.hairs
