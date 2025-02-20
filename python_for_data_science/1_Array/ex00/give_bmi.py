def give_bmi(height: list[int | float], weight: list[int | float]) \
  -> list[int | float]:
    """Calculate BMI (Body Mass Index) for pairs of height and weight values.

    Args:
        height (list[int | float]): List of heights in meters
        weight (list[int | float]): List of weights in kilograms

    Returns:
        list[int | float]: List of calculated BMI values

    Raises:
        ValueError: If height and weight lists have different lengths

    The zip() function in Python is a built-in function that aggregates
    elements from multiple iterables (like lists, tuples, etc.) into a
    single iterator of tuples. Each tuple contains the i-th element
    from each of the input iterables.
    """
    # Check if input lists have the same length
    if len(height) != len(weight):
        raise ValueError("height and weight must have the same length")
    # Calculate BMI for each height-weight pair using list comprehension
    return [w / h ** 2 for h, w in zip(height, weight)]


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    """Check which BMI values exceed a given limit.

    Args:
        bmi (list[int | float]): List of BMI values
        limit (int): BMI threshold value

    Returns:
        list[bool]: List of boolean values, True if BMI exceeds limit
    """
    return [x > limit for x in bmi]
