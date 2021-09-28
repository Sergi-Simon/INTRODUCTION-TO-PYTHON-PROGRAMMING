
def Sqrt ( a, *args ):
	nmax =1000
	tol=1.e-20	
	if len(args)>0:
		nmax=args[0]
		if len(args)>1:
			tol=args[1]
	x0 = 1
	Abs = 1
	x=x0
	i=0
	while Abs >= tol and i<nmax:
		X = 0.5* (x+(a/x))
		Abs = abs(X-x)
		x=X
		i+=1
	if i>=nmax:
		print("precision not reached")
	return X

def f1 ( x ):
	return Sqrt(x**2+1)

def f2 ( x ):
	return 1/(x**2-2)
