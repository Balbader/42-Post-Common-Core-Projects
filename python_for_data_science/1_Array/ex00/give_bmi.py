def give_bmi(height: list[int | float], weight: list[int | float]) \
  -> list[int | float]:
    # Check if input lists have the same length
    if len(height) != len(weight):
        raise ValueError("height and weight must have the same length")
    # Calculate BMI for each height-weight pair using list comprehension
    # The zip() function in Python is a built-in function that aggregates
    # elements from multiple iterables (like lists, tuples, etc.) into a
    # single iterator of tuples. Each tuple contains the i-th element
    # from each of the input iterables.
    return [w / h ** 2 for h, w in zip(height, weight)]


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    # Return list of boolean values indicating if each BMI exceeds the limit
    return [x > limit for x in bmi]
