import time

class ProfilingDecorator(object):
    def __init__(self, f) -> None:
        self.f = f
    
    def __call__(self, *args):
        start_time = time.time()
        result = self.f(n)
        end_time = time.time()
        print("[Time elapsed for n = {}] {}".format(n, end_time - start_time))

        return result

class ToHTMLDecorator(object):
    def __init__(self, f):
        print("HTML wrapper initiated")
        self.f = f
        
    def __call__(self, *args):
        print("ToHTMLDecorator called")
        return "<html><body>{}</body></html>".format(self.f(*args))
    
def generate_n(n: int):
    i = 2
    while i < n:
        yield i
        i += 1

@ToHTMLDecorator
@ProfilingDecorator
def fib(n: int) -> int:
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