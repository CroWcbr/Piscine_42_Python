from sys import argv, stdin
from string import punctuation


def text_analyzer(*args) -> None:
    """
    This function counts the number of upper characters, lower characters,
    punctuation and spaces in a given text.
    """
    if len(args) > 1:
        print("AssertionError: more than one argument are provided")
        return
    elif len(args) == 0 or (len(args) == 1 and args[0] == "None"):
        print("What is the text to analyze?")
        print(">>", end=' ')
        s = stdin.readline()
    else:
        s = args[0]

    if not isinstance(s, str):
        print("AssertionError: argument is not a string")
        return

    LOWER = sum(1 for char in s if char.islower())
    UPPER = sum(1 for char in s if char.isupper())
    PUNC = sum(1 for char in s if char in punctuation)
    SPACE = sum(1 for char in s if char.isspace())
    LEN = len(s)
    DIGIT = sum(1 for char in s if char.isdigit())
    print("The text contains", LEN, "character(s):")
    print(UPPER, "upper letters")
    print(LOWER, "lower letters")
    print(PUNC, "punctuation marks")
    print(SPACE, "spaces")
    print(DIGIT, "digits")


if __name__ == "__main__":
    if (len(argv) == 1):
        text_analyzer()
    else:
        text_analyzer(*argv[1:])
