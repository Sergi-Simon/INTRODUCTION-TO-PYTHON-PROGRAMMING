""" methods.py
	Solution to the coursework
    Author: Sergi Simon
    Latest update: June 30, 2021
"""

import functions as fu
import numpy as np


def Householder( p, jet, x0, tol, maxit, filename  ):

	print( p )

	if p+1 != len(jet):
		print( "you need to set your records straight" )
		return [0]

	length = len( jet )
	x = x0
	aux = 1
	i = 0
	file = open(filename, "w")
	file.write("{:d} \t {:.20f} \n".format(0,x))
	while aux >= tol and i <= maxit:
		i += 1
		X=G(x,p,jet)
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

def G ( x, p, jet ):

	f = jet[0](x)

	df = jet[1](x)
	if p == 1:
		return x - f/df 

	ddf = jet[2](x)
	if p == 2:
		return (2 * df * f)/(-2.*df*df+ddf*f)+x

	dddf = jet[3](x)
	if p == 3:
		return (3.*f*(-2.*df*df + ddf*f))/(6*df*df*df - 6*ddf*df*f + dddf*f*f) + x

	ddddf = jet[4](x)
	if p == 4:
		return (4.*f*(6.*df*df*df - 6.*ddf*df*f + dddf*f*f))/(-24.*df*df*df*df + 36.*ddf*df*df*f - 2*(3*ddf*ddf + 4.*dddf*df)*f*f + ddddf*f*f*f) + x


