from sys import argv

morse_dict = {' ': '/',
              'A': '.-',
              'B': '-...',
              'C': '-.-.',
              'D': '-..',
              'E': '.',
              'F': '..-.',
              'G': '--.',
              'H': '....',
              'I': '..',
              'J': '.---',
              'K': '-.-',
              'L': '.-..',
              'M': '--',
              'N': '-.',
              'O': '---',
              'P': '.--.',
              'Q': '--.-',
              'R': '.-.',
              'S': '...',
              'T': '-',
              'U': '..-',
              'V': '...-',
              'W': '.--',
              'X': '-..-',
              'Y': '-.--',
              'Z': '--..',
              '1': '.----',
              '2': '..---',
              '3': '...--',
              '4': '....-',
              '5': '.....',
              '6': '-....',
              '7': '--...',
              '8': '---..',
              '9': '----.',
              '0': '-----'}


def main():
    try:
        assert len(argv) == 2, "wrong number of arguments"
        list_of_word = argv[1].upper().split()
        assert all(word.isalnum() for word in list_of_word), "wrong symbol"
    except AssertionError as msg:
        print("Assertion Error: " + str(msg))
        return -1

    print(
        " / ".join(
            " ".join(morse_dict[char] for char in word)
            for word in list_of_word
        )
    )


if __name__ == "__main__":
    main()
