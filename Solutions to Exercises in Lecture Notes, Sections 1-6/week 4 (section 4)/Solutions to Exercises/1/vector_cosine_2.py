""" vector_cosine.py
	Program returnning the cosine of two vectors with loops
	Author: Sergi Simon
	Last update: October 26, 2020 """

import math

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

# this will be easier with exception throwing
def vector_cos( listx, listy ):
	tol = 1.e-14
	cosine = dot_product(listx,listy)/(math.sqrt(dot_product(listx,listx)*dot_product(listy,listy)))
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
x = take_input(2,"x")
y = take_input(2,"y")
print("The dot product is",dot_product(x,y))
cosine = vector_cos( x, y )
print("The cosine of their angle is",cosine)
