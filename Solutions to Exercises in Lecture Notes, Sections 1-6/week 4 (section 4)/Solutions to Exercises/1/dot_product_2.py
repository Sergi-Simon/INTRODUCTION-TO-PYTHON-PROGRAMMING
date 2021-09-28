""" dot_product_2.py
	Program returning dot product with loops
	Author: Sergi Simon
	Last update: October 27, 2020 """

# Bear in mind that this program will be easier with loops than it is with recursive functions


def take_input( n, string ):
	list1=[]
	for i in range(n):
		x = float(input(string+"["+str(i)+"] = "))
		list1.append(x)
	return(list1)

def dot_product ( listx, listy ):
	s = 0
	for i in range(len(listx)):	
		s += listx[i]*listy[i]
	return s

n = int(input("Write a positive integer larger than or equal to 2: "))
x = take_input(n,"x") 
y = take_input(n,"y")
print("The dot product is",dot_product(x,y))


