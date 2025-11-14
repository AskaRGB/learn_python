import logging
import sys
from functools import wraps


def log(filename=None):
    """Декоратор логирования работы функции"""
    if filename:
        logging.basicConfig(filename=filename, level=logging.INFO, format="%(message)s")
    logging.basicConfig(level=logging.INFO, stream=sys.stdout, format="%(message)s")

    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            try:
                result = func(*args, **kwargs)
                logging.info(f"{func.__name__}  ok")
                print(f"{func.__name__}  ok")
                return result
            except Exception as e:
                logging.error(f"{func.__name__} error: {type(e).__name__}. Inputs {args}, {kwargs}")
                print(f"{func.__name__} error: {type(e).__name__}. Inputs {args}, {kwargs}")
                raise

        return wrapper

    return decorator


@log()
def summ(x, y):
    return x / y


print(summ(1, 2))
