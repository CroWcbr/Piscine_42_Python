from S1E7 import Baratheon, Lannister


class King(Baratheon, Lannister):
    """Сlass King inherited from Baratheon and Lannister."""

    def set_eyes(self, eyes):
        """set King eyes."""
        self.eyes = eyes

    def set_hairs(self, hairs):
        """set King hairs."""
        self.hairs = hairs

    def get_eyes(self):
        """get King eyes."""
        return self.eyes

    def get_hairs(self):
        """get King hairs."""
        return self.hairs
