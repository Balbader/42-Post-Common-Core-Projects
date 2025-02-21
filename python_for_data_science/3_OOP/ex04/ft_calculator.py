class calculator:
    """A class for vector calculations."""

    @staticmethod
    def dotproduct(V1: list[float], V2: list[float]) -> None:
        """Calculate and print the dot product of two vectors."""
        result = sum(x * y for x, y in zip(V1, V2))
        print(f"Dot product is: {result}")

    @staticmethod
    def add_vec(V1: list[float], V2: list[float]) -> None:
        """Calculate and print the addition of two vectors."""
        result = [x + y for x, y in zip(V1, V2)]
        print(f"Add Vector is : {result}")

    @staticmethod
    def sous_vec(V1: list[float], V2: list[float]) -> None:
        """Calculate and print the subtraction of two vectors."""
        result = [x - y for x, y in zip(V1, V2)]
        print(f"Sous Vector is: {result}")
