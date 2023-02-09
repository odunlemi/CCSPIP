# A first recursive attempt
# A fibonacci sequence is a sequence of numbers such that any number, 
#      except for the first and second is a sum of the previous two

# Taking the sequence
#    0, 1, 1, 2, 3, 5, 8, 13, 21...
#It follows tat to get the value of any Fibonacci number, n, in the sequence,
#   one can use the formula

#   fib(n) = fib( n -1 ) + fib( n - 2 )

# A recursive Fibonacci function that translates the above formula
def fib1(n: int) -> int:
    return fib1(n-1) + (n-2)

if __name__ == "__main__":
    print(fib1(5))

#Outputs to an infifnte recursion