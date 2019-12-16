import functools
import time



def my_timer(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print("Go Go Go: 00.00.00s ")
        start_time = time.perf_counter()
        value = func(*args, **kwargs) #assigment  needed if wrapped fun returns sth
        stop_time = time.perf_counter()
        elapsed_time = stop_time-start_time
        print(f"time passed by: {elapsed_time}")
        return value # returns value from func u will use wrapper on
    return wrapper



@my_timer
def do_stuff(n):
    for i in range(n):
        print("i")
    return 'zombie zombie zombie '  #just for sake of testing wrapper
x = do_stuff(5)
print(x)