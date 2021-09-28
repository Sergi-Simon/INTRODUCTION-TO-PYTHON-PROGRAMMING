""" functions.py
	Solution to the coursework
    Author: Sergi Simon
    Latest update: June 30, 2021
"""

import math
import numpy as np

fx0 = 0
fx1 = 2


def f1 ( x ):
	return math.cos( x )
def df1 ( x ):
	return -math.sin( x )
def ddf1 ( x ):
	return -math.cos( x )
def dddf1 ( x ):
	return math.sin( x )
def ddddf1 ( x ):
	return math.cos( x )	

def f2 ( x ):
	return math.exp( -x ) - x
def df2 ( x ):
	return -math.exp( -x ) - 1
def ddf2 ( x ):
	return math.exp( -x ) 
def dddf2 ( x ):
	return -math.exp( -x ) 
def ddddf2 ( x ):
	return math.exp( -x ) 


def f3 ( x ):
	return x**2 + 4*x -1
def df3 ( x ):
	return 2*x + 4
def ddf3 ( x ):
	return 2
def dddf3 ( x ):
	return 0
def ddddf3 ( x ):
	return 0


def f4 ( x ):
	return np.float64(math.cos( math.exp(x**2 + 1)) - x)
def df4 ( x ):
	aux = x**2+1
	aux2 = math.exp(aux)
	return -2.*aux2*x *math.sin(aux2)-1
def ddf4 ( x ):
	xsq = x**2
	aux = xsq+1
	aux2 = math.exp(aux)
	return -2*aux2*(2*aux2*xsq*math.cos(aux2)+(1+2*xsq)*math.sin(aux2))
def dddf4 ( x ):
	xsq = x**2
	aux = xsq+1
	aux2 = math.exp(aux)
	return 4*aux2*x*(-3*aux2*(1+2*xsq)*math.cos(aux2)+(-3+2*(-1+aux2**2)*xsq)*math.sin(aux2))
def ddddf4 ( x ):
	xsq = x**2
	aux = xsq+1
	aux2 = math.exp(aux)
	return 4*aux2*(aux2*(-3+4*(-7+aux2**2)*xq-36*xsq)*math.cos(aux2)+(-3+4*xsq*(-3-xsq+aux2**2*(3+6*xsq)))*math.sin(aux2))

