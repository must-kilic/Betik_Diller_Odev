from functools import wraps
import time

def timer(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        t0 = time.perf_counter()
        result = func(*args, **kwargs)
        total_time = time.perf_counter() - t0
        print(f"total_time: {total_time:.5f} saniye")
        return result
    return wrapper


def required_column(requireds: set[str]):
    def deco(func):
        @wraps(func)
        def wrapper(path, *args, **kwargs):
            result = func(path, *args, **kwargs)
            if not result:
                raise ValueError("Boş veri seti")
            keys = set(result[0].keys())
            print(f"Verideki kolonlar: {keys}")
            missing = requireds - keys
            if missing:
                raise ValueError(f"Eksik kolon(lar): {missing}")

            return result
        return wrapper
    return deco
