""" interpolation.py
    Solution to the coursework
    Author: Sergi Simon
    Latest update: October 27, 2019 """

import time
import matplotlib.pyplot as plt
import numpy as np
import sys

# Function to read data from a file: 
def read_from_file( string, tol ):
	k = 0
	string2=string
	while True:
		try:
			F = open( string2, "r" )
			F1 =F.readlines()
			F.close()
			break
		except: 
			if k>=5: 
				return 0
			print("We could not open file: chance {} out of 5 to add it to the same directory".format(k))
			string2=input("Write a proper name for this file")
			k+=1
		
	x=[]
	y=[]
	for v in F1:
		u = v.split()
		if len(u) != 2:
			return -1
		xk = float(u[0])
		yk = float(u[1])
		for i in x: 
			if abs(i-xk) < tol:
				return -2
		x.append(xk)
		y.append(yk)
	return x,y



def deflate ( mat, i, j ):
    mat1=np.delete(mat, i, 0)
    mat1=np.delete(mat1, j, 1)
    return mat1

def det ( mat ):
    shape = mat.shape
    if len(shape) != 2:
        print( "This is not a matrix")
        return []
    if shape[0] != shape[1]:
        print ("This is not a square matrix")
        return []
    if shape==(1,1):
        return mat[0,0]
    if shape == (2,2):
        return mat[0,0]*mat[1,1] - mat[0,1]*mat[1,0]
    n = shape[0]
    s = 0
    p = 1
    for j in range(n):
        mat1=deflate( mat, 0, j )
        s += mat[0,j]*det(mat1)*p
        p = -p
    return s


def Cramer ( mat, b ):
    shape = mat.shape
    x=[]
    if shape[0] != shape[1]:
        print("Your matrix is not square")
        return -1
    det_a = det(mat)
    n = shape[0]
    for j in range(n):
        mat1 = np.copy(mat)
        for i in range(n):
            mat1[i,j]=b[i]
        det1=det(mat1)
        x.append(det1/det_a)
    return x


# Horner's method
def Horner ( A, x ):
	n = len(A)
	U = A[-1]
	rev = list(reversed(range(n)))
	rev.pop()
	for k in rev:
		U = U * (x)
		U = U + A[k-1]
	return U 

# write to files
def write_to_files( shortfilename, longfilename, npoints, listx, listy, mat, coeff, a, b, store ):
	global xarray
	global yarray
	shortfile = open(shortfilename, "w")
	longfile = open(longfilename, "w")
	for i in range(len(mat)):
		for j in range(len(mat)):
			shortfile.write("%.20f\t" % mat[i,j])
		shortfile.write("\n")
	
	for i in range(len(listy)):
		shortfile.write("%.20f\t" % listy[i])
	shortfile.write("\n")

	for i in range(len(coeff)):
		shortfile.write("%.20f\t" % coeff[i])
	shortfile.write("\n")


	shortfile.close()

	x = a
	step = (b-a)/float(npoints-1)
	for i in range(npoints):
		y = Horner(coeff,x)
		longfile.write("{:.20f} \t {:.20f} \n".format(x,y))
		if store == 1:
			xarray.append(x)
			yarray.append(y)
		x = x+step
	longfile.close()


def VandermondeSolution ( listx, listy ):
	list2=[]
	np1=len(listx)
	for i in range(np1):
		s=1
		list1=[s]
		for j in range(np1-1):
			s *= listx[i]
			list1.append(s)
		list2.append(list1)
	mat = np.asarray(list2, dtype=np.float64)
	a = Cramer( mat, listy ) 
	return  mat, a
 

def main ():

	
	name = sys.argv[1]	
	numits = int(sys.argv[2])
	data = read_from_file(name, 1.e-10)

	if data == 0:
		print("You need to place the file in the same directory as your Python file")
	elif data == -1:
		print("You need to fill out the data file properly")
	elif data == -2:
		print("abscissae too close by standards of ", 100)
	else:
		x,y=data

		print("Your abscissae " ,x)
		print("Your ordinates " ,y)
		print("this is a representation of the points in the Cartesian plane:")
		plt.plot(x, y,'ro') 
		plt.axes().set_aspect('equal', 'datalim')
		# naming the x axis 
		#plt.xlabel('x - axis') 
		# naming the y axis 
		#plt.ylabel('y - axis') 
		# giving a title to my graph 
		plt.title('Graph of the original points')   
		# function to show the plot 
		plt.show() 

		a = min(x)-0.2 #0.05
		b = max(x)+0.2 #0.05
		# recursive
		start = time.time()
		V,coeff = VandermondeSolution ( x, y )
		coeff = Cramer(V,y)
		end = time.time()
		global xarray, yarray
		xarray=[]
		yarray=[]
		print("The time taken is: ",end - start)
		write_to_files("matrix_and_vectors.txt", "function_to_plot.txt", numits, x, y, V, coeff, a, b, 1 )
		plt.plot(xarray, yarray,'k,') 
		plt.axes().set_aspect('equal', 'datalim')
		# naming the x axis 
		#plt.xlabel('x - axis') 
		# naming the y axis 
		#plt.ylabel('y - axis') 
		# giving a title to my graph 
		

		plt.title('Graph of the interpolating polynomial')   
		# function to show the plot 
		plt.show() 

		plt.figure()
		plt.plot(xarray, yarray, 'k', x, y, 'ro')
		plt.axes().set_aspect('equal', 'datalim')
		plt.title('Graph of the interpolating polynomial and the original points') 
		plt.show()

		plt.figure()
		plt.plot(xarray, yarray, 'k', x, y, 'ro')
		plt.title('Same graph, aspect ratio adapted') 
		plt.show()


if __name__ == '__main__':
    main()
