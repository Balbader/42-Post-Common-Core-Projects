import sys
from ft_filter import ft_filter


def main():
    """
    Main function to filter strings based on length
    This function takes two arguments:
    - A string of words separated by spaces
    - An integer n
    It filters the words in the string to include
    only those with length greater than n and prints the result.
    """
    try:
        # Check if we have exactly 2 arguments (excluding script name)
        assert len(sys.argv) == 3, "the arguments are bad"

        # Get the string and number from arguments
        string = sys.argv[1]
        n = sys.argv[2]

        # Verify types
        assert isinstance(string, str), "the arguments are bad"
        assert n.isdigit(), "the arguments are bad"
        n = int(n)

        # Split string into words and filter
        words = string.split()
        result = list(ft_filter(lambda x: len(x) > n, words))

        print(result)

    except AssertionError as e:
        print(f"AssertionError: {e}")


if __name__ == "__main__":
    main()
