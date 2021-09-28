""" zeros.py
    Solution to the coursework
    Author: Sergi Simon
    Latest update: October 31, 2020 """

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
	global method
	if method == "B":
		Method = "Bisection"
	if method == "S":
		Method = "Secant"
	if method == "N":
		Method = "Newton"	
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
	plt.text(a+xxrange/20., ymin+yrange/10.,"for "+str(function)+" with ")
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
	typical call: zeros [option] [method] [name] [f] [df] [x0] [x1]
	"""
	global option, x0, x1, name, method, f, df, function
	print( sys.argv )
	if len( sys.argv ) > 1:
		option = int( sys.argv[1] )	# keyboard or database
		method = sys.argv[2] # method chosen: S, N, B
		name = sys.argv[3] # name of the file where we will write the iterations
	
	# if we are going to take the functions from keyboard
	if option == 0:
		function = sys.argv[4]
		f = lambda x : string_to_f_with_x( x, function )
		#codeblock = """def f(x):\n\treturn %s""" % function
		#exec(codeblock)
		print( f( 0 ))
		if method == 'N':
			dfunction = sys.argv[5]
			df = lambda x : string_to_f_with_x( x, dfunction )
			#codeblockd = """df = lambda x : %s""" % dfunction
			#exec(codeblockd)
	# if we are going to take the functions from the function database
	elif option > 0 and option <= 5:
		print ( "we are taking function "+str(option)+" in your function list")
		function = "fu.f"+str(option)
		f = lambda x : string_to_f( x, function )
		if method == 'N':
			dfunction = "fu.df"+str(option)
			df = lambda x : string_to_f( x, dfunction )
	else:
		print ( "we are taking the first function in your function list because you're not writing a proper option")
		
	if len( sys.argv ) > 6:
		x0 = float( sys.argv[6] )
		if len( sys.argv ) > 7:
			x1 = float( sys.argv[7] )

	print("Your initial conditions " ,x0, x1)
	print("let us start by plotting your function:")
	initial_plot ( f, x0, x1, 500 )
	print("Your initial conditions after plot" ,x0, x1)
	
	if method == 'S':
		output = me.Secant( f, x0, x1, 1.e-16, 200, name )
	elif method == 'N':
		output = me.Newton( f, df, x0, 1.e-16, 200, name )
	else:
		output = me.Bisection( f, x0, x1, 1.e-15, 500, name )

	print( output )
	if len( output ) == 2:
		print( "Your method has converged to {:.20f}".format(output[0]))
		final_plot ( f, name )
	else:
		print( "Your method has not converged in the required amount of iterations")

# in case we are not inputting them from keyboard
x0 = fu.fx0
x1 = fu.fx1
def f(x):
	return fu.f1(x)
def df(x):
    return fu.df1(x)
option = 1
method = 'N'
name = "newtoncos.txt"
function = "cos( x )"

if __name__ == '__main__':	
    main()
