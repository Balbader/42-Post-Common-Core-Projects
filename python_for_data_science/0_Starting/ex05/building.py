import sys
import string


def count_characters(text):
    """Count different types of characters in the given text."""
    upper_count = sum(1 for c in text if c.isupper())
    lower_count = sum(1 for c in text if c.islower())
    punct_count = sum(1 for c in text if c in string.punctuation)
    digit_count = sum(1 for c in text if c.isdigit())
    space_count = sum(1 for c in text if c.isspace())

    total = len(text)

    print(f"The text contains {total} characters:")
    print(f"{upper_count} upper letters")
    print(f"{lower_count} lower letters")
    print(f"{punct_count} punctuation marks")
    print(f"{space_count} spaces")
    print(f"{digit_count} digits")


def main():
    # Check number of arguments
    if len(sys.argv) > 2:
        raise AssertionError("more than one argument provided")

    # Get text from argument or user input
    if len(sys.argv) == 2:
        text = sys.argv[1]
    else:
        print("What is the text to count?")
        try:
            text = input()
        except EOFError:  # Handle Ctrl+D
            return

    count_characters(text)


if __name__ == "__main__":
    try:
        main()
    except AssertionError as e:
        print(f"AssertionError: {e}")
