def square(x: int | float) -> int | float:
    """square"""
    return x ** 2


def pow(x: int | float) -> int | float:
    """pow"""
    return x ** x


def outer(x: int | float, function) -> object:
    """outer"""
    count = 0

    def inner() -> float:
        nonlocal count
        nonlocal x

        count += 1
        x = function(x)
        return x
    return inner
