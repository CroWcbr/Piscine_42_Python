from typing import Any


def callLimit(limit: int):
    """callLimit"""
    count = 0

    def callLimiter(function):
        """callLimiter"""
        def limit_function(*args: Any, **kwds: Any):
            """limit_function"""
            nonlocal count
            if count < limit:
                count += 1
                return function(*args, **kwds)
            else:
                print(f"Error: <function {function.__name__} "
                      f"at {hex(id(function))}> call too many times")
        return limit_function
    return callLimiter
