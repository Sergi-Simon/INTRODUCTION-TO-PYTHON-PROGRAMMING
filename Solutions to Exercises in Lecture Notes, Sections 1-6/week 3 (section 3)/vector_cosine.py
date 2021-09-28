""" vector_cosine.py
	Program returnning the cosine of two vectors with recursive functions
	Author: Sergi Simon
	Last update: October 26, 2020 """

import math

def take_input( n, string, list0 ):
	list1=list0.copy() # you can also write list1=list0 and it will still work
	if len( list1 ) == n:
		return list1
	x = float(input(string+"["+str(len(list1))+"] = ")) # str transforms that number to a string
	list1.append(x)
	return take_input( n, string, list1 )

#this will be easier with loops
def dot_product ( listx, listy, index, value ):
	if index == len (listx):
		return value
	s = listx[index]*listy[index]
	return dot_product ( listx, listy, index+1, value+s )

# this will be easier with exception throwing
def vector_cos( listx, listy ):
	tol = 1.e-14
	cosine = dot_product(listx,listy,0,0)/(math.sqrt(dot_product(listx,listx,0,0)*dot_product(listy,listy,0,0)))
	if abs(cosine - 1) < tol: 
		print ("The vectors are collinear and in the same direction")
		return cosine 
	if abs(cosine + 1) < tol: 
		print ("The vectors are collinear and in opposite directions")
		return cosine 
	if abs(cosine) < tol: 
		print ("The vectors are perpendicular")
		return cosine 
	print ("The vectors are neither perpendicular nor collinear")
	return cosine 

print("Write the two vectors: ")
x = take_input(2,"x",[])
y = take_input(2,"y",[])
print("The dot product is",dot_product(x,y,0,0))
cosine = vector_cos( x, y )
print("The cosine of their angle is",cosine)
