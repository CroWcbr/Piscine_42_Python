import random
import string
from dataclasses import dataclass, field


def generate_id() -> str:
    """generate_id method"""
    return "".join(random.choices(string.ascii_lowercase, k=15))


@dataclass
class Student:
    """Student class"""
    name: str
    surname: str
    active: bool = True
    login: str = field(init=False, default_factory=lambda: 'Eagle')
    id: str = field(init=False, default_factory=generate_id)
