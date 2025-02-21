import random
import string
from dataclasses import dataclass, field


def generate_id() -> str:
    """
    Generate a random ID of 15 lowercase letters
    Returns:
        str: A random ID of 15 lowercase letters
    """
    return "".join(random.choices(string.ascii_lowercase, k=15))


@dataclass
class Student:
    """
    A class representing a student
    """
    name: str
    surname: str
    active: bool = True
    login: str = field(init=False)
    id: str = field(init=False, default_factory=generate_id)

    def __post_init__(self):
        self.login = self.name[0].upper() + self.surname.capitalize()
