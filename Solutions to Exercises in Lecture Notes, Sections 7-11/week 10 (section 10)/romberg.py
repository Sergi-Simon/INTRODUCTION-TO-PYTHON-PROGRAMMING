from trapezium.compositetrapezium import *
#from trapezium.functions import *
#from trapezium.taylorfunctions import *

import numpy as np
import matplotlib.pyplot as plt

def buildup( func, a, b, min_n, max_n, exact_integral ):
	x=[]
	y=[]
	X=[]
	Y=[]
	XX=[]
	YY=[]
	n = min_n
	diff = b-a
	while n <= max_n:
		h = diff/float(n)
		integral=romberg(func,a,b,n,1)
		x.insert(0,h)
		y.insert(0,abs(exact_integral-integral))
		integral=romberg(func,a,b,n,2)
		X.insert(0,h)
		Y.insert(0,abs(exact_integral-integral))
		integral=romberg(func,a,b,n,3)
		XX.insert(0,h)
		YY.insert(0,abs(exact_integral-integral))
		
		n+=1
	return x,y,X,Y,XX,YY


def romberg ( func, a, b, n, k ):
	if k==1:
		return trapezium(func,a,b,n)
	else:
		return (2**k*romberg(func,a,b,2*n,k-1)-romberg(func,a,b,n,k-1))/float(2**k-1)

def main( ):

	x, y, X,Y ,XX,YY= buildup( np.cos,1,3, 10, 2000, -0.70035097674802928455 )
	y=np.log(y)
	Y=np.log(Y)
	YY=np.log(YY)
	
	plt.plot(x, y,'r.',X,Y,"g.",XX,YY,"k.")
	plt.show()

	
if __name__ =='__main__': 
	main()

