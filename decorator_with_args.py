import functools


def repeater(_func=None, *, num_of_repeats=1):
    def my_decorator(func):
        @functools.wraps(func)
        def wrapper(*args,**kwargs):

            for _ in range(num_of_repeats):
                value_func = func(*args, **kwargs)
            return value_func

        return wrapper
    if _func is None:
        return my_decorator
    else:
        return my_decorator(_func)

@repeater(num_of_repeats=3)
def some_func():
    print("Race")
some_func()