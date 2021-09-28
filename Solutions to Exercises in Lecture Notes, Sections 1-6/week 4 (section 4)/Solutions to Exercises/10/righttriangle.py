""" righttriangle.py
	Program producing a right triangle of numbers
	Author: Sergi Simon
	Last update: October 28, 2020 """


def print_right_triangle ( n ):
	s=1
	for i in range(n):
		for j in range(i+1):
			print(s, end="\t")
			s+=1
		print("")


n = int(input("Write a positive integer larger than or equal to 2: "))
print_right_triangle(n)
