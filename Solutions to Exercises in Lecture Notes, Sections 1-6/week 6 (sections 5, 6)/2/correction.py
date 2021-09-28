""" correction.py
	program correcting the first exercise
	Author: Sergi Simon
	Last Update: November 4, 2020 """

x=int(input("Write an integer x>1"))
y=int(input("Write another integer y<-2"))
if x <= 1 and y >= -2:
	print("Both are wrong numbers")
elif y >= -2:
	print("x is correct but y is not")
elif x <= 1:
	print("y is correct but x is not")
else:
	print("both numbers are as requested")