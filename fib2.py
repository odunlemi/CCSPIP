# Utilizing base cases to avoid infifnte recursion
# In a recursive function, a base case serves as a stopping point

# In the case of the the Fibonacci sequence, 
#   we have natural base cases in the form of the special first two sequence values 0 and 1
# Neither 0 nor 1 is the sum of the previous two numbers in the sequence

# Specifying 0 and 1 as base cases
def fib2(n: int) -> int:
    if n < 2:   #base case
        return n
    return fib2(n -2) + (n - 1) #recursive case