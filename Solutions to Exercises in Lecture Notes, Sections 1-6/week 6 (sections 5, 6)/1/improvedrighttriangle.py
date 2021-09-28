""" improvedrighttriangle.py
	Improved program producing a right triangle of numbers
	Author: Sergi Simon
	Last update: October 28, 2020 """


def print_right_triangle ( n ):
	s=1
	for i in range(n):
		for j in range(i+1):
			print(s, end="\t")
			s+=1
		print("")


counter = 0
while True:
	try:
		n = int(input("Write a positive integer larger than or equal to 2: "))
		print_right_triangle(n)
		break
	except: 
		counter += 1
		if counter == 5:
			print("you've had enough chances")
			break
		print("Keep trying...")

