""" primeQimproved.py
	Improved program asking for a number and deciding whether it is prime
	Author: Sergi Simon
	Last update: October 28, 2020 """


def try_prime( n ):
	i = 2
	while n % i != 0:
		i+=1
	if i == n:
		print(str(n) + " is prime")
	else:
		print(str(n) + " is not prime")

counter = 0
while True:
	try:
		n = int(input("Write a positive integer larger than 2: "))
		try_prime(n)
		break
	except: 
		counter += 1
		if counter == 10:
			print("you've had enough chances")
			break
		print("Keep trying...")

