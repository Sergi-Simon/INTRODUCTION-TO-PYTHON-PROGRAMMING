""" dot_product.py
	Program returning dot product with a recursive function
	Author: Sergi Simon
	Last update: October 26, 2020 """

# Bear in mind that this program will be easier with loops than it is with recursive functions


def take_input( n, string, list0 ):
	list1=list0.copy() # you can also write list1=list0 and it will still work
	if len( list1 ) == n:
		return list1
	x = float(input(string+"["+str(len(list1))+"] = ")) # str transforms that number to a string
	list1.append(x)
	return take_input( n, string, list1 )

def dot_product ( listx, listy, index, value ):
	if index == len (listx):
		return value
	s = listx[index]*listy[index]
	return dot_product ( listx, listy, index+1, value+s )

n = int(input("Write a positive integer larger than or equal to 2: "))
x = take_input(n,"x",[]) 
y = take_input(n,"y",[])
print("The dot product is",dot_product(x,y,0,0))


