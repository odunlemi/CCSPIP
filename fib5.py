# Solving Fibonacci with an iterative approach
def fib5(n: int) -> int:
    if n == 0: return n  # special case
    last: int = 0  # intially set to fib(0)
    next: int = 1  # intially set to fib(1)
    
    # The for loop uses tuple unpacking; it is more concise

    #   The thing is last is being set to the previous value of next 
    #       and next is being set to the previous value of last plus the previous value of next.
    # This avoids the creation of a temp variable to hold the old value of next
    #     after last is updated but before next is updated. 

    # With this approcah, the for loop will run n-1  times
    # So for the 20th Fibonacci number -> (20 - 1) = 19 times
    # Compare 19 iterative runs to 21,891 recursive calls of the same
    for _ in range(1, n):
        last, next = next, last + next
    return next

if __name__ == "__main__":
    print(fib5(0))
    print(fib5(10))
    print(fib5(50))
    print(fib5(100))