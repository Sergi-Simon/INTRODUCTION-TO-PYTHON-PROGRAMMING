""" binomial.py
    Program that computes binomial coefficients
    Author: Sergi Simon
    Last update: October 22, 2020 """

def factorial ( n ):
    if n<0:
        print ("We cannot compute the factorial of ", n, " because it is negative")
        # We return a value that we know is impossible; integer factorials cannot be -1
        return 0
    if n==0:
        return 1
    return n*factorial(n-1)

def binomial ( n, k ):
    if k>n:
        print("We cannot compute this binomial because the second number is larger than the first")
        # We return a value that we know is impossible; binomial coefficients cannot be -1
        return -1
    var1=factorial(n)
    if var1<0:
        print ("We cannot compute this binomial because the factorial of ", n," could not be computed") 
        # We return a value that we know is impossible; binomial coefficients cannot be -2
        return -2
    var2=factorial(k)
    if var2<0:
        print ("We cannot compute this binomial because the factorial of ", k," could not be computed") 
        # We return a value that we know is impossible; binomial coefficients cannot be -3
        return -3
    var3=factorial(n-k)
    return int(var1/(var2*var3))

n=int(input("Write number n: "))
k=int(input("Write number k: "))
var=binomial(n,k)
if var<0:
    print ("Please run the program again with adequate values")
else:
    print( "The binomial coefficient is ", binomial(n,k))
