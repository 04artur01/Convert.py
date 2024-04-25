from functools import wraps
import time


def timer(func):
    """
    Decorator to measure the execution time of a function.

    This decorator calculates the time taken by a function to execute and prints the duration in seconds.

    Args:
        func (callable): The function to be decorated.

    Returns:
        callable: The decorated function.
    """
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"Execution time of {func.__name__}: {end - start} seconds")
        return result

    return wrapper


def measure_time(func):
    """
    Decorator to measure the execution time of a function.

    This decorator calculates the time taken by a function to execute and prints the duration in seconds.

    Args:
        func (callable): The function to be decorated.

    Returns:
        callable: The decorated function.
    """
    def wrapper():
        start = time.time()
        func()
        end = time.time()
        print(f"Execution time: {end - start} seconds")

    return wrapper


def debug(func):
    """
    Decorator to print function call details for debugging purposes.

    This decorator prints the function name, arguments, and return value for debugging purposes.

    Args:
        func (callable): The function to be decorated.

    Returns:
        callable: The decorated function.
    """
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__} with args: {args} and kwargs: {kwargs}")
        result = func(*args, **kwargs)
        print(f"{func.__name__} returned: {result}")
        return result

    return wrapper


def memoize(func):
    """
    Decorator to memoize function results.

    This decorator caches the results of a function call based on its arguments, so that if the same arguments are
    provided again, the cached result is returned instead of re-executing the function.

    Args:
        func (callable): The function to be decorated.

    Returns:
        callable: The decorated function.
    """
    cache = {}

    @wraps(func)
    def wrapper(*args):
        if args in cache:
            return cache[args]
        else:
            result = func(*args)
            cache[args] = result
            return result

    return wrapper
