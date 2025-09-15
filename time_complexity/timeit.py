import time
import functools
import asyncio

def timeit(func):
    """
    Decorator to measure the execution time of synchronous and asynchronous functions.
    Prints the time taken to execute the function.
    Args:
        func (callable): The function to be decorated.
    Returns:
        callable: The wrapped function with timing functionality.
    Usage:
        @timeit
        def my_function():
            # function implementation

        @timeit
        async def my_async_function():
            # async function implementation
    """
    if asyncio.iscoroutinefunction(func):
        @functools.wraps(func)
        async def async_wrapper(*args, **kwargs):
            start = time.perf_counter()
            result = await func(*args, **kwargs)
            end = time.perf_counter()
            print(f"[{func.__name__}] executed in {end - start:.4f} seconds")
            return result
        return async_wrapper
    else:
        @functools.wraps(func)
        def sync_wrapper(*args, **kwargs):
            start = time.perf_counter()
            result = func(*args, **kwargs)
            end = time.perf_counter()
            print(f"[{func.__name__}] executed in {end - start:.4f} seconds")
            return result
        return sync_wrapper