class calculator:
    """A calculator class for vector-scalar operations."""

    def __init__(self, vector):
        """Initialize calculator with a vector.

        Args:
            vector (list): List of numbers representing a vector
        """
        self.vector = vector

    def __add__(self, scalar) -> None:
        """Add scalar to each element of the vector and print result.

        Args:
            scalar (int/float): Number to add to each vector element
        """
        result = [x + scalar for x in self.vector]
        print(result)

    def __mul__(self, scalar) -> None:
        """Multiply each vector element by scalar and print result.

        Args:
            scalar (int/float): Number to multiply each vector element by
        """
        result = [x * scalar for x in self.vector]
        print(result)

    def __sub__(self, scalar) -> None:
        """Subtract scalar from each vector element and print result.

        Args:
            scalar (int/float): Number to subtract from each vector element
        """
        result = [x - scalar for x in self.vector]
        print(result)

    def __truediv__(self, scalar) -> None:
        """Divide each vector element by scalar and print result.

        Args:
            scalar (int/float): Number to divide each vector element by

        Raises:
            ZeroDivisionError: If scalar is zero
        """
        if scalar == 0:
            raise ZeroDivisionError("Cannot divide by zero")
        result = [x / scalar for x in self.vector]
        print(result)
