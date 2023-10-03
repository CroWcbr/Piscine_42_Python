from S1E9 import Character


class Baratheon(Character):
    """Сlass Baratheon inherited from Character."""
    def __init__(self, first_name, is_alive=True):
        """Initialize Baratheon character with first name and alive status."""
        super().__init__(first_name, is_alive)
        self.family_name = 'Baratheon'
        self.eyes = 'brown'
        self.hairs = 'dark'

    def __str__(self):
        """Baratheon return a string repr of the character."""
        return f"Vector: ('{self.family_name}', '{self.eyes}', '{self.hairs}')"

    def __repr__(self):
        """Baratheon return a string repr of the character for debugging."""
        return self.__str__()

    def die(self):
        """Baratheon method die."""
        self.is_alive = False


class Lannister(Character):
    """Сlass Lannister inherited from Character."""
    def __init__(self, first_name, is_alive=True):
        """Initialize Lannister character with first name and alive status."""
        super().__init__(first_name, is_alive)
        self.family_name = 'Lannister'
        self.eyes = 'blue'
        self.hairs = 'light'

    def __str__(self):
        """Lannister return a string repr of the character."""
        return f"Vector: ('{self.family_name}', '{self.eyes}', '{self.hairs}')"

    def __repr__(self):
        """Lannister return a string repr of the character for debugging."""
        return self.__str__()

    def die(self):
        """Lannister method die."""
        self.is_alive = False

    @classmethod
    def create_lannister(cls, first_name, is_alive=True):
        """Create Lannister characters in a chain."""
        return cls(first_name, is_alive)
