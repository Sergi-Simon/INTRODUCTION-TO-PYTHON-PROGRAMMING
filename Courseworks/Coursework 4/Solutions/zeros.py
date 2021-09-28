""" zeros.py
    Solution to the ref/def coursework
    Author: Sergi Simon
    Latest update: June 30, 2021 """

import time
import math
import methods as me
import functions as fu
import matplotlib.pyplot as plt
import sys
import numpy as np

def initial_plot ( f, a, b, npoints ):
	global x0
	global x1
	xarray = []
	yarray = []
	
	x = a
	step = (b-a)/float(npoints-1)
	for i in range(npoints):
		y = f(x)
		xarray.append(x)
		yarray.append(y)
		x = x+step
	
	plt.figure()
	plt.plot(xarray, yarray, 'k')
	plt.plot([min(xarray),max(xarray)],[0,0],'r-',lw=1)
	#plt.axes().set_aspect('equal', 'datalim')
	plt.title('Initial graph, interval adjusted to ['+str(a)+','+str(b)+']')
	plt.show()
	print( "Satisfied? If not, write the extremes of a new interval; otherwise write 0")
	k = input( ).split()
	if len( k ) == 2:
		aa = float( k[0] )
		bb = float( k[1] )
		x0 = aa
		x1 = bb
		initial_plot( f, aa, bb, npoints )

def final_plot ( f, filename ):
	npoints = 1000
	
	array,Xarray = read_from_file( filename )
	
	a = min( Xarray ) - 0.05
	b = max( Xarray ) + 0.05
	
	while True:
		plot_label( a, b, array, Xarray )
		out = input( "Write 0 if you wish to stop, or an interval if you wish to zoom in or out")
		Out = out.split()
		if len( Out ) == 1:
			break
		elif len( Out ) == 2:
			a = float( Out[0] )
			b = float( Out[1] )
			plot_label( a, b, array, Xarray )
		else:
			print( "you did not write a proper input")
			break

	
	

	
# function plottinh with labels
def plot_label ( a, b, array, Xarray ):
	global p, jet
	f = lambda x:jet[0](x)
	Method = "p="+str(p)
	
	x = a
	npoints = 1000
	xarray = []
	yarray = []
	step = (b-a)/float(npoints-1)
	for i in range(npoints):
		y = f(x)
		xarray.append(x)
		yarray.append(y)
		x = x+step
	ymin = min(f(a),f(b))
	ymax = max(f(a),f(b))
	xxrange = (b-a)
	yrange = ymax-ymin
	plt.figure()
	plt.xlim(a, b)
	plt.ylim(ymin-0.05, ymax+0.05)
	plt.plot(xarray, yarray, 'k')
	plt.plot(Xarray, np.zeros(len(Xarray)), 'ro')
	for k in array:
		print( k )
		if k < max(array):
			if a <= Xarray[k] <= b and abs( Xarray[k] - Xarray[k+1] ) >= (b-a)/100:
				label = "$x_{:d}$".format(k)
				plt.annotate( label, (Xarray[k],0), textcoords="offset points", xytext=(0,10), ha='center')  
	plt.plot([a,b],[0,0],'r-',lw=1)
	plt.text(a+xxrange/20., ymin+yrange/20., Method+" converged to "+str(Xarray[-1]))
	plt.text(a+xxrange/20., ymin+yrange/10.,"for function"+str(fun)+" with ")
	plt.title('Final graph, interval adjusted to ['+str(a)+','+str(b)+']')
	plt.show()	

# Function to read first and last column from a file: 
def read_from_file( string ):
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
	
	firstlength = len(F1[0].split())

	x=[]
	y=[]
	for v in F1:
		u = v.split()
		if len(u) != firstlength:
			print( " this file is not arrayed in columns ")
			return -1
		xk = int(u[0])
		yk = float(u[-1])
		x.append(xk)
		y.append(yk)
	return x,y



def string_to_f( x, func ):
    try:
        fx = eval(func)(x)
        return fx
    except:
        return 0

def string_to_f_with_x( x, func ):
    try:
        fx = eval(func)
        return fx
    except:
        return 0
        
def main ():
	
	"""
	typical call: zeros [f] [p] [name] [x0] [x1]
	"""
	global p, x0, x1, name, fun, jet
	print( sys.argv )
	if len( sys.argv ) > 1:
		fun = int( sys.argv[1] )
		p = int( sys.argv[2] ) # method chosen
		name = sys.argv[3] # name of the file where we will write the iterations
		
	# if we are going to take the functions from the function database
	print ( "we are taking function "+str(fun)+" in your function list")
	basicstr = "f"
	labels = ["fu."+basicstr+str(fun)]
	for i in range( 1, p+1 ):
		basicstr = "d"+basicstr
		labels.append("fu."+basicstr+str(fun))

	jet = [lambda x, i=i : string_to_f( x, labels[i] ) for i in range(p+1) ]
	
	if len( sys.argv ) == 1:
		print ( "we are taking the first function in your function list because you're not writing a proper option")
		
	if len( sys.argv ) >= 5:
		x0 = float( sys.argv[4] )
		if len( sys.argv ) >= 6:
			x1 = float( sys.argv[5] )

	print("Your initial conditions " ,x0, x1)
	print("let us start by plotting your function:")
	initial_plot ( jet[0], x0, x1, 500 )
	print("Your initial conditions after plot" ,x0, x1)
	
	
	output = me.Householder( p, jet, x0, 1.e-16, 200, name  )
		
	print( output )
	if len( output ) == 2:
		print( "Your method has converged to {:.20f}".format(output[0]))
		final_plot ( jet[0], name )
	else:
		print( "Your method has not converged in the required amount of iterations")


# in case we are not inputting them from keyboard
x0 = fu.fx0
x1 = fu.fx1
fun = 1
jet = [fu.f1,fu.df1,fu.ddf1,fu.dddf1]
p = 3
name = "cos3.txt"

if __name__ == '__main__':	
    main()
