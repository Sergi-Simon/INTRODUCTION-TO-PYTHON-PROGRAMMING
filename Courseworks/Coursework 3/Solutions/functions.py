""" functions.py
	Solution to the coursework
    Author: Sergi Simon
    Latest update: October 31, 2020
"""

import math
import numpy as np

fx0 = 0
fx1 = 2


def f1 ( x ):
	return math.cos( x )
def df1 ( x ):
	return -math.sin( x )


def f2 ( x ):
	return math.exp( -x ) - x
def df2 ( x ):
	return -math.exp( -x ) - x

def f3 ( x ):
	return x**2 + 4*x -1
def df3 ( x ):
	return 2*x* + 4

def f4 ( x ):
	return np.float64(math.cos( math.exp(x**2 + 1)) - x)
def df4 ( x ):
	aux = x**2+1
	aux2 = math.exp(aux)
	return -2.*aux2*x *math.sin(aux2)-1

def f5( x ):
	return math.exp(-x**2)
