""" primeQ.py
	Program asking for a number and deciding whether it is prime
	Author: Sergi Simon
	Last update: October 28, 2020 """


def try_prime( n ):
	i = 2
	while n % i != 0:
		i+=1
	if i == n:
		return(str(n) + " is prime")
	return(str(n) + " is not prime")

n = int(input("Write a positive integer larger than 2: "))
print( try_prime(n) )