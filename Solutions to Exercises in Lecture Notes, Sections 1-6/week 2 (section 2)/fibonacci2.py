""" fibonacci2.py
    Routine that computes any Fibonacci number with a non-recursive function
    Author: Sergi Simon
    Last update: October 22, 2020  """

# this is necessary if we want to be able to call sqrt
import math

# These constants can be defined globally because our function will only use them, but will not re-define them
phi = 1+math.sqrt(5) # this is usually called the golden ratio 
phi = 0.5*phi
psi = -1/phi
print( "The golden ratio is equal to ", phi )
print( "The negative inverse of the golden ratio is equal to ", psi )

# function
def fib2 ( n ):
    var1 = (phi**n)-(psi**n)
    var2 = var1 / math.sqrt(5)
    return int(var2)

# We take n as keyboard input
n=int(input( "Write the value of n "))

# We return the requested value
print("Fibonacci number F_", n," is ", fib2(n))
