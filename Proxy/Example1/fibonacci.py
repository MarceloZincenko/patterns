import time

class Caculator(object):
    def Calculator(self, n: int, cache: dict) -> int:
        
        if n < 2:
            return 1
        
        if n in cache:
            return cache[n]
        
        cache[n] = self.fib_cached(n - 2, cache) + self.fib_cached(n - 1, cache)
        return cache[n]

if __name__ == "__main__":
    calc = Calculator()
    cache = {}
    start_time = time.time()
    fib_sequence = [calc.fib_cached(x, cache) for x in range(0, 80)]
    end_time = time.time()
    print(
        "Calculating the list of {} Fibonacci numbers took {} seconds".format(
        len(fib_sequence),
        end_time - start_time
    ))
    