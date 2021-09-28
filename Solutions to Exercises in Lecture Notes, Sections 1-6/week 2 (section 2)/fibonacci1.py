""" fibonacci1.py
    Routine that computes any Fibonacci number with a recursive function
    Author: Sergi Simon
    Last update: October 22, 2020  """

def fib1 ( n ):
    if n==0:
        return 0
    if n==1:
        return 1
    return fib1(n-1)+fib1(n-2)

# We take n as keyboard input
n=int(input( "Write the value of n "))

# We return the requested value
print("Fibonacci number F_", n," is ", fib1(n))
