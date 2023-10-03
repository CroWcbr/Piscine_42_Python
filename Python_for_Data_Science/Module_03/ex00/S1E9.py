from abc import ABC, abstractmethod


class Character(ABC):
    """Abstract base class for characters."""
    def __init__(self, first_name, is_alive=True):
        """Initialize a character with a first name and an is_alive status."""
        self.first_name = first_name
        self.is_alive = is_alive

    @abstractmethod
    def die(self):
        """ Abstract method to change the character's status."""
        pass


class Stark(Character):
    """Сlass Stark inherited from Character."""
    def die(self):
        """Stark method to change the character's status."""
        self.is_alive = False
