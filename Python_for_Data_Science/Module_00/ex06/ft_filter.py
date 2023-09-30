def ft_filter(function, iterable):
    '''filter(function or None, iterable) --> filter object
Return an iterator yielding those items of iterable for which function(item)
is true. If function is None, return the items that are true.'''
    if not callable(function):
        raise TypeError("function must be a callable function")
    return [x for x in iterable if function(x)]


if __name__ == "__main__":
    print(filter.__doc__)
    try:
        numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        filtered_numbers = ft_filter(lambda x: x > 5, numbers)
        print(list(filtered_numbers))  # Output: [2, 4, 6, 8]
    except TypeError as e:
        print(f"Error: {e}")
