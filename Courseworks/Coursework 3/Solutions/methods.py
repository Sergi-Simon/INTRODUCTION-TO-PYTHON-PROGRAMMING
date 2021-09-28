""" methods.py
	Solution to the coursework
    Author: Sergi Simon
    Latest update: October 31, 2020
"""

import matplotlib.pyplot as plt
import functions as fu
import numpy as np

def Newton( f, df, x0, tol, maxit, filename  ):
	x = x0

	aux = 1
	i = 0
	file = open(filename, "w")
	file.write("{:d} \t {:.20f} \n".format(0,x))
	while aux >= tol and i <= maxit:
		i += 1
		X=x-f(x)/df(x)
		file.write("{:d} \t {:.20f} \n".format(i,X))
		aux = abs( x-X )
		if aux < tol:
			print( "found our approximation at iteration"+str(i))
		x = X
	file.close()
	if aux < tol:
		return [X, i]
	if aux >= tol:
		return [i]

def Secant( f, x0, x1, tol, maxit, filename  ):
	aux = 1
	i = 0
	file = open(filename, "w")
	file.write("{:d} \t {:.20f} \t {:.20f} \n".format(0,x0,x1))
	x = x0
	xx = x1 
	while aux >= tol and i <= maxit:
		i += 1
		xxx = xx - f(xx) *( xx - x ) /( f(xx) - f(x) )
		file.write("{:d} \t {:.20f} \t {:.20f} \n".format(i,xx,xxx))
		aux = abs( xxx-xx )
		if aux < tol:
			print( "found our approximation at iteration"+str(i))
		x = xx
		xx = xxx
	file.close()
	if aux < tol:
		return [xxx, i]
	if aux >= tol:
		return [i]

def Bisection( f, x0, x1, tol, maxit, filename  ):
	if f( x0 ) * f( x1 ) >= 0.:
		print( "Your interval does not work" )
	aux = 1
	i = 0
	file = open(filename, "w")
	x = x0
	xx = x1
	while aux >= tol and i <= maxit:
		i += 1
		aux = abs( x-xx )
		c = (x+xx)/2.
		file.write("{:d} \t {:.20f} \t {:.20f} \t {:.20f} \n".format(i-1,x,xx,c))
		if aux < tol:
			print( "found our approximation at iteration"+str(i))
			break

		""" this creates problems if f(x), f(xx) and f(c) are too small
		if f(x)*f(c) < 0:
			xx = c
		elif f(xx)*f(c) < 0:
			x = c """

		if ( f(x) < 0 and f(c) > 0 ) or ( f(x) > 0 and f(c) < 0 ):
			xx = c
		elif ( f(xx) < 0 and f(c) > 0 ) or ( f(xx) > 0 and f(c) < 0 ):
			x = c
		
	file.close()
	if i <= maxit:
		return [c, i]
	else:
		return [i]
