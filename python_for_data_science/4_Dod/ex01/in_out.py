def square(x: int | float) -> int | float:
    """Calculate the square of a number.

    Args:
        x (int | float): The number to be squared

    Returns:
        int | float: The square of the input number
    """
    return x * x


def pow(x: int | float) -> int | float:
    """Calculate x raised to the power of x.

    Args:
        x (int | float): The base and exponent number

    Returns:
        int | float: x raised to the power of x
    """
    return x ** x


def outer(x: int | float, function) -> object:
    """Create a closure that repeatedly applies a function to a value.

    Args:
        x (int | float): Initial value
        function: Function to be applied (either square or power)

    Returns:
        object: Inner function that keeps track of the number of applications
                and returns the result of applying the function
    """
    count = 0

    def inner() -> float:
        """Apply the function to x based on the number of previous calls.

        Returns:
            float: Result of applying the function to x
        """
        nonlocal x, count
        if count == 0:
            result = function(x)
        else:
            result = function(x)
            for _ in range(count):
                x = result
                result = function(x)
        count += 1
        return result
    return inner
