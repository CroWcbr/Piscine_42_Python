from sys import argv
from ft_filter import ft_filter


def filterstring(S: str, N: int):
    """
    This function output a list of words
    from S that have a length greater than N.
    """
    words = S.split()
    result = ft_filter(lambda word: len(word) > N, words)
    return list(result)


def main():
    try:
        assert len(argv) == 3, "not enough arguments"
        assert isinstance(argv[1], str), \
               "invalid first argument, must be a string"
        assert all(char.isalnum() or char.isspace() for char in argv[1]), \
               "the string contains special characters"
        assert argv[2].isdigit(), "invalid first argument, must be a int"
    except AssertionError as msg:
        print("Assertion Error: " + str(msg))
        return -1

    print(filterstring(argv[1], int(argv[2])))


if __name__ == "__main__":
    main()
