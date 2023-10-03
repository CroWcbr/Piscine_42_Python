class calculator:
    """Calculator class"""
    def __init__(self, numbers):
        """Initialize calculator with a vector."""
        self.numbers = numbers

    def __add__(self, object) -> None:
        """add method"""
        self.numbers = [ele + object for ele in self.numbers]
        print(self.numbers)

    def __mul__(self, object) -> None:
        """mul method"""
        self.numbers = [ele * object for ele in self.numbers]
        print(self.numbers)

    def __sub__(self, object) -> None:
        """sub method"""
        self.numbers = [ele - object for ele in self.numbers]
        print(self.numbers)

    def __truediv__(self, object) -> None:
        """truediv method"""
        if object == 0:
            raise ZeroDivisionError("Division by zero")
        self.numbers = [ele / object for ele in self.numbers]
        print(self.numbers)
