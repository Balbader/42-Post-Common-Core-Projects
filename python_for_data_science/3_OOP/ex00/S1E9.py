from abc import ABC, abstractmethod

""" This implementation:
Creates an abstract base class Character with abstract
methods __init__ and die

Creates a concrete Stark class that inherits from Character
and implements the required methods

Includes proper docstrings for all classes and methods
Handles the required parameters (first_name and optional is_alive)
Implements the die() method to change is_alive to False

The code will work with the provided test cases
and will raise a TypeError if someone tries to instantiate
the abstract Character class directly.
"""


class Character(ABC):
    """A Game of Thrones character class"""

    @abstractmethod
    def __init__(self, first_name: str, is_alive: bool = True):
        """Constructor for Character class

        Args:
            first_name (str): The character's first name
            is_alive (bool, optional): Character's living status.
                        Defaults to True
        """
        self.first_name = first_name
        self.is_alive = is_alive

    @abstractmethod
    def die(self):
        """Method to change the character's living status to False"""
        self.is_alive = False


class Stark(Character):
    """A class representing the Stark family members"""

    def __init__(self, first_name: str, is_alive: bool = True):
        """Constructor for Stark class

        Args:
            first_name (str): The Stark family member's first name
            is_alive (bool, optional): Character's living status.
                        Defaults to True
        """
        super().__init__(first_name, is_alive)

    def die(self):
        """Method to change the Stark member's living status to False"""
        super().die()
