def ft_statistics(*args: any, **kwargs: any) -> None:
    """Calculate and print various statistical measures based on input numbers.

    This function computes different statistical measures
        (mean, median, quartiles,
    standard deviation, variance) based on the provided keyword arguments.

    Args:
        *args: Variable number of numeric values to perform calculations on.
        **kwargs: Operations to perform, valid values are:
            - "mean": arithmetic mean
            - "median": middle value of sorted numbers
            - "quartile": first (Q1) and third (Q3) quartiles
            - "std": standard deviation
            - "var": variance

    Returns:
        None. Results are printed to standard output.
        If no numbers are provided,
                prints "ERROR" for each requested operation.
    """

    # If no numbers provided in args, print ERROR for each kwarg
    if len(args) == 0:
        for _ in kwargs:
            print("ERROR")
        return

    # Convert args to list and sort it for calculations
    numbers = sorted(list(args))
    n = len(numbers)

    for operation in kwargs.values():
        if operation == "mean":
            mean = sum(numbers) / n
            print(f"mean : {mean}")

        elif operation == "median":
            mid = n // 2
            median = numbers[mid] \
                if n % 2 else (numbers[mid-1] + numbers[mid]) / 2
            print(f"median : {median}")

        elif operation == "quartile":
            q1_pos = n // 4
            q3_pos = (3 * n) // 4
            q1 = float(numbers[q1_pos])
            q3 = float(numbers[q3_pos])
            print(f"quartile : [{q1}, {q3}]")

        elif operation == "std":
            mean = sum(numbers) / n
            variance = sum((x - mean) ** 2 for x in numbers) / n
            std = variance ** 0.5
            print(f"std : {std}")

        elif operation == "var":
            mean = sum(numbers) / n
            variance = sum((x - mean) ** 2 for x in numbers) / n
            print(f"var : {variance}")
