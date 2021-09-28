""" exponential.py
    Program that computes approximations of the exponential function recursively
    Author: Sergi Simon
    Last update: October 22, 2020 """

def factorial ( n ):
    if n==0:
        return 1
    return n*factorial(n-1)

def f( x, k ):
    if k==0:
        return 1
    var = (x**k)/factorial(k) + f(x,k-1)
    return var

x=float(input("Write the value of x whose exponential e^x you want to approximate "))
k=int(input("Write the degree k of the approximation "))
print ("The desired approximation is ", f(x,k))

# You can test this program, say, by fixing a certain value of x, for instance
# x=3.4. Start running the program for increasing values of k. The larger k is,
# the closer the output will be to what you would obtain if you pressed e^x and 3.4
# in your calculator. For k=30 the output will be correct in its first 14 decimal digits
# and will stay correct for them in higher k: 29.96410004739701
