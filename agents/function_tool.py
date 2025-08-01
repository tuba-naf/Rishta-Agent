import functools
import inspect

def function_tool(func):
    @functools.wraps(func)
    def sync_wrapper(*args, **kwargs):
        print(f"🔧 Running function: {func.__name__} (sync)")
        return func(*args, **kwargs)

    @functools.wraps(func)
    async def async_wrapper(*args, **kwargs):
        print(f"🔧 Running function: {func.__name__} (async)")
        return await func(*args, **kwargs)

    return async_wrapper if inspect.iscoroutinefunction(func) else sync_wrapper
