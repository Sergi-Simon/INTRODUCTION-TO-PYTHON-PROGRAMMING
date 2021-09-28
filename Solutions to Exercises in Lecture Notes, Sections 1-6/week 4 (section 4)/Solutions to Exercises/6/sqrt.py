""" sqrt.py
	Program computing the square root of any positive number
	Author: Sergi Simon
	Last update: October 28, 2020 """


def Sqrt ( a, nmax, tol ):
	x0 = 1
	Abs = 1
	x=x0
	i=0
	while Abs >= tol and i<nmax:
		X = 0.5* (x+(a/x))
		Abs = abs(X-x)
		x=X
		i+=1
	if Abs < tol:
		print("precision goal has been achieved")
	else:
		print("number of iterations has been reached")
	return X

print( "The square root of 2 with 3 iterations is "+str(Sqrt( 2, 3, 1.e-15 )))
print( "The square root of 2 with a maximum of 100 iterations is "+str(Sqrt( 2, 100, 1.e-15 )))
print( "The square root of 3 with a maximum of 100 iterations is "+str(Sqrt( 3, 100, 1.e-15 )))
print( "The square root of 5 with a maximum of 100 iterations is "+str(Sqrt( 5, 100, 1.e-15 )))
print( "The square root of 4 with a maximum of 100 iterations is "+str(Sqrt( 4, 1000, 1.e-15 )))