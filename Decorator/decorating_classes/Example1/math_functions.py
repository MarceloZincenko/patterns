from profilers import profile_all_class_methods, profiling_wrapper

@profile_all_class_methods
class DoMathStuff(object):
    def generate_n(self, n: int):
        i = 2
        while i < n:
            yield i
            i += 1

    def fib(self, n: int) -> int:
        if n < 2:
            return
        
        prev_fib = 1
        fib = 1
        for _ in self.generate_n(n):
            prev_fib, fib = fib, fib + prev_fib
        
        return fib
    
    @profiling_wrapper
    def factorial(self, n:int):
        res = 1
        for i in self.generate_n(n):
            res *= i
        return res
