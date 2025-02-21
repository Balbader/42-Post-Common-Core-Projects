def callLimit(limit: int):
    """
    Decorator factory that creates a decorator to limit function calls
    Args:
        limit (int): Maximum number of times the function can be called
    """
    count = 0

    def callLimiter(function):
        """
        Decorator that limits the number of times a function can be called
        Args:
            function: The function to be decorated
        """
        def limit_function(*args: any, **kwds: any):
            """
            Limit the number of times a function can be called
            Args:
                *args: Positional arguments
                **kwds: Keyword arguments
            Returns:
                The result of the function call
            """
            nonlocal count
            if count >= limit:
                print(f"Error: {function} call too many times")
                return
            count += 1
            return function(*args, **kwds)
        return limit_function
    return callLimiter
