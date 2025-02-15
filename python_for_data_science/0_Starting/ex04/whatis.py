import sys

def main():
    try:
        # Check if more than one argument is provided
        if len(sys.argv) > 2:
            raise AssertionError("more than one argument is provided")

        # If no argument is provided, exit silently
        if len(sys.argv) == 1:
            sys.exit()

        # Try to convert argument to integer
        num = int(sys.argv[1])

        # Check if number is even or odd
        if num % 2 == 0:
            print("I'm Even.")
        else:
            print("I'm Odd.")

    except ValueError:
        raise AssertionError("argument is not an integer")

if __name__ == "__main__":
    main()
