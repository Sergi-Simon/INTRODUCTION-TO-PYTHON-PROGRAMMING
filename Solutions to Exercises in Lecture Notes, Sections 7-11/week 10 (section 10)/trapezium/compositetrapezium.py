#from functions import *
#from taylorfunctions import *


""" this is the slower method (applying trapezium without optimising operations)
def trapezium ( func, a, b, *args ):
	if len(args)==0:
		return 0.5*(func(a)+func(b))*(b-a)
	n = args[0]
	h = (b-a)/float(n)
	x0 = a
	s=0
	for i in range(n):
		x1 = x0+h
		s += trapezium(func,x0,x1)
		x0=x1
	return s
"""


# method that optimises operations 
def trapezium ( func, a, b, *args ):
	if len(args)==0:
		return 0.5*(func(a)+func(b))*(b-a)
	n = args[0]
	h = (b-a)/float(n)
	x0 = a
	s=0
	for i in range(1,n):
		x0+=h
		s += func(x0)
		
	s = 2.*s + func(a) + func(b)
	s *= 0.5*h
	return s


def main ():
	print("composite trapezium!")
	print(trapezium(Cos,1,3,10000))
	print(trapezium(Sqrt,2,10,20000))
	print(trapezium(f1,-1,1,10000))
	print(trapezium(f2,0,1,2000))
	print(trapezium(Sin,2,7,2000))
	print(trapezium(Cosh,0,1,10000))
	print(trapezium(Sinh,0,2,2000))
	print(trapezium(exp,-10,1,2000))
	print(trapezium(lnoneminus,0.2,0.6))
	

if __name__ =='__main__': 
	main()


