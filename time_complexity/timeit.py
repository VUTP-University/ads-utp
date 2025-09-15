import time
import functools
import asyncio

def timeit(func):
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