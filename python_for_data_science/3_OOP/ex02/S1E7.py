from S1E9 import Character


class Baratheon(Character):
    """Representing the Baratheon family."""

    def __init__(self, first_name, is_alive=True):
        """Initialize a Baratheon character."""
        super().__init__(first_name, is_alive)
        self.family_name = "Baratheon"
        self.eyes = "brown"
        self.hairs = "dark"

    def __str__(self):
        """Return string representation of Baratheon character."""
        return f"Vector: ('{self.family_name}', '{self.eyes}', '{self.hairs}')"

    def __repr__(self):
        """Return official string representation of Baratheon character."""
        return self.__str__()

    def die(self):
        """Kill the character."""
        self.is_alive = False


class Lannister(Character):
    """Representing the Lannister family."""

    def __init__(self, first_name, is_alive=True):
        """Initialize a Lannister character."""
        super().__init__(first_name, is_alive)
        self.family_name = "Lannister"
        self.eyes = "blue"
        self.hairs = "golden"

    def __str__(self):
        """Return string representation of Lannister character."""
        return f"Vector: ('{self.family_name}', '{self.eyes}', '{self.hairs}')"

    def __repr__(self):
        """Return official string representation of Lannister character."""
        return self.__str__()

    def die(self):
        """Kill the character."""
        self.is_alive = False

    @classmethod
    def create_lannister(cls, first_name, is_alive=True):
        """Create a new Lannister character."""
        return cls(first_name, is_alive)
