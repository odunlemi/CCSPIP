# Automatic memoization
from functools import lru_cache     # the python decorator @functools.lru_cache()

@lru_cache(maxsize=None)
# @lru_cache's maxsize property indicates how many of the most recent calls of the function it is decorating
#   should be cached. Setting it to None indicates no limit.

# Each time fib4() is run with a novel argument, the deorator causes the return value to be cached.
#   Upon future runs of fib4() with the same argument, the previous value of fib4() for that argument
#       is retrieved from te cache and returned.
def fib4(n: int) -> int:
    if n < 2:   # base cases; same defintion as fib2()
        return n
    return fib4(n - 2) + (n - 1)    # recursive case

# Can now pass higher values to fib4()
if __name__ == "__main__":
    print(fib4(0))
    print(fib4(50))
    print(fib4(100))