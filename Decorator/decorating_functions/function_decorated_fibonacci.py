import time
from functools import wraps

def ProfilingDecorator(f):
    def wrapped_f(n):
        start_time = time.time()
        result = f(n)
        end_time = time.time()
        print("[Time elapsed for n = {}] {}".format(n, end_time - start_time))

        return result
    
    return wrapped_f

def ProfilingDecorator_wrapped(f):
    @wraps(f) # to mantain f name after decorated
    def wrapped_f(n):
        start_time = time.time()
        result = f(n)
        end_time = time.time()
        print("[Time elapsed for n = {}] {}".format(n, end_time - start_time))

        return result
    
    return wrapped_f

   
def generate_n(n: int):
    i = 2
    while i < n:
        yield i
        i += 1

@ProfilingDecorator
def fib(n: int) -> int:
    if n < 2:
        return
    
    prev_fib = 1
    fib = 1
    for _ in generate_n(n):
        prev_fib, fib = fib, fib + prev_fib
    
    return fib

@ProfilingDecorator_wrapped
def fib_wrapped(n: int) -> int:
    if n < 2:
        return
    
    prev_fib = 1
    fib = 1
    for _ in generate_n(n):
        prev_fib, fib = fib, fib + prev_fib
    
    return fib

if __name__ == "__main__":
    n = 7700
    print("Fibonacci number for n = {}: {}".format(n, fib(n)))
    f = fib
    f_w = fib_wrapped
    print("Function to be decorated: ", f.__name__) #does not mantains fib name
    print("Function to be decorated: ", f_w.__name__) #mantains fib name
