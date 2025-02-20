def slice_me(family: list, start: int, end: int) -> list:
    """Slice a 2D array (family) based on start and end indices.

    Args:
        family (list): A 2D array (list of lists)
        start (int): The starting index of the slice
        end (int): The ending index of the slice

    Returns:
        list: A new list containing the sliced elements

    Raises:
        TypeError: If input is not a list of lists
        ValueError: If lists have different sizes or indices are invalid
    """
    # Check if family is a list and contains lists
    if not isinstance(family, list) or not all(isinstance(row, list) for row in family):
        raise TypeError("Input must be a list of lists")

    # Check if the array is empty
    if not family or not family[0]:
        raise ValueError("Empty array")

    # Check if all rows have the same length
    row_length = len(family[0])
    if not all(len(row) == row_length for row in family):
        raise ValueError("All rows must have the same length")

    # Print original shape
    print(f"My shape is : ({len(family)}, {row_length})")

    # Create sliced array
    result = family[start:end]

    # Print new shape
    print(f"My new shape is : ({len(result)}, {row_length})")

    return result
