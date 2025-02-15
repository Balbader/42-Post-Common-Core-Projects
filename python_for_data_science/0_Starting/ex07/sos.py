import sys

NESTED_MORSE = {
    " ": "/ ",
    "A": ".- ",
    "B": "-... ",
    "C": "-.-. ",
    "D": "-.. ",
    "E": ". ",
    "F": "..-. ",
    "G": "--. ",
    "H": ".... ",
    "I": ".. ",
    "J": ".--- ",
    "K": "-.- ",
    "L": ".-.. ",
    "M": "-- ",
    "N": "-. ",
    "O": "--- ",
    "P": ".--. ",
    "Q": "--.- ",
    "R": ".-. ",
    "S": "... ",
    "T": "- ",
    "U": "..- ",
    "V": "...- ",
    "W": ".-- ",
    "X": "-..- ",
    "Y": "-.-- ",
    "Z": "--.. ",
    "0": "----- ",
    "1": ".---- ",
    "2": "..--- ",
    "3": "...-- ",
    "4": "....- ",
    "5": "..... ",
    "6": "-.... ",
    "7": "--... ",
    "8": "---.. ",
    "9": "----. "
}


def main():
    """
    Main function to convert text to Morse code
    This function takes one argument:
    - A string of text to convert to Morse code
    It converts the text to Morse code and prints the result.
    """

    # Check if exactly one argument is provided
    if len(sys.argv) != 2:
        raise AssertionError("the arguments are bad")

    text = sys.argv[1]
    result = ""

    # Convert each character to Morse code
    try:
        for char in text.upper():
            if char not in NESTED_MORSE:
                raise AssertionError("the arguments are bad")
            result += NESTED_MORSE[char]
    except Exception:
        raise AssertionError("the arguments are bad")

    # Print result without the trailing space
    print(result.rstrip())


if __name__ == "__main__":
    try:
        main()
    except AssertionError as e:
        print(f"AssertionError: {str(e)}")
