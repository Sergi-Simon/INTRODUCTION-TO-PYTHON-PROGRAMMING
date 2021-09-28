""" max_out_of_three.py
	program finding the maximum of three numbers
	Author: Sergi Simon
	Last Update: November 4, 2020 """

def max_out_of_three (x, y, z):
	
	if x < y:
		if y < z:
			return z
		else:
			return y
	else:
		if x < z:
			return z
		else: 
			return x


x = int(input("write x"))
y = int(input("write y"))
z = int(input("write z"))

print ("The maximum is ", max_out_of_three(x,y,z))