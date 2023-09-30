from sys import argv


def main():
    if len(argv) == 1:
        return
    elif len(argv) != 2:
        print("AssertionError: more than one argument are provided")
        return

    try:
        argument = int(argv[1])
    except ValueError:
        print("AssertionError: argument is not an integer")
        return

    if argument % 2 == 0:
        print("I'm Even")
    else:
        print("I'm Odd")


if __name__ == "__main__":
    main()
