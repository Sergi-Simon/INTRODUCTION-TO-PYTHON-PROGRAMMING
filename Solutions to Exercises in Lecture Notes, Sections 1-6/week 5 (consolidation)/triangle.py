""" triangle.py
	Program producing an isosceles triangle of alternating-sign numbers
	Author: Sergi Simon
	Last update: November 4, 2020 """


def print_triangle ( n ):
	s=1
	spaces = n-1
	for i in range(n):
		for j in range(spaces):
			print("\t",end="")	
		for j in range(2*i+1):
			print(s, end="\t")
			s*=-2
		spaces-=1
		print("")


counter = 0
while True:
	try:
		n = int(input("Write a positive integer larger than or equal to 2: "))
		print_triangle(n)
		break
	except: 
		counter += 1
		if counter == 5:
			print("you've had enough chances")
			break
		print("Keep trying...")

