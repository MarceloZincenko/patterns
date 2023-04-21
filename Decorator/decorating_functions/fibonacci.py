import time

def generate_n(n: int):
    i = 2
    while i < n:
        yield i
        i += 1

def fib(n: int) -> int:
    if n < 2:
        return
    
    prev_fib = 1
    fib = 1
    for _ in generate_n(n):
        prev_fib, fib = fib, fib + prev_fib
    
    return fib

def profile_me(f, n: int) -> time:
    start_time = time.time()
    result = f(n)
    end_time = time.time()
    print("[Time elapsed for n = {}] {}".format(n, end_time - start_time))

    return result

def get_profiled_function(f):
    return lambda n: profile_me(f, n)

if __name__ == "__main__":
    n = 7700
    fib_profiled = get_profiled_function(fib)
    print("Fibonacci number for n = {}: {}".format(n, fib_profiled(n)))