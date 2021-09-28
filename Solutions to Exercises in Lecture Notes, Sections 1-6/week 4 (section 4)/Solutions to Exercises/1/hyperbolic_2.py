""" hyperbolic.py
    Program that computes approximations of the hyperbolic sine and cosine
    Author: Sergi Simon
    Last update: October 28, 2020 """

# These were already in exponential.py
def factorial ( n ):
    if n==0:
        return 1
    return n*factorial(n-1)

def f( x, k ):
    if k==0:
        return 1
    var = (x**k)/factorial(k) + f(x,k-1)
    return var

# These are new
def Cosh(x,k):
    var1 = f(x,k)
    var2 = f(-x,k)
    var3 = var1+var2
    var3 = 0.5*var3
    return var3

def Sinh(x,k):
    var1 = f(x,k)
    var2 = f(-x,k)
    var3 = var1-var2
    var3 = 0.5*var3
    return var3

# We ask the user to input the values of x and k
x=float(input("Write the value of x whose hyperbolic functions you want to approximate "))
k=int(input("Write the degree k of the approximation for the exponential"))
# We compute and return the output
print ("The approximation for the hyperbolic cosine is ", Cosh(x,k))
print ("The approximation for the hyperbolic sine is ", Sinh(x,k))

# You can test this program, say, by fixing a certain value of x
# Start running the program for increasing values of k. The larger k is,
# the closer the output will be to what you would obtain if you pressed cosh and sinh
# in your calculator. 
