from functions import *
from taylorfunctions import *

def trapezium ( func, a, b ):
	return 0.5*(func(a)+func(b))*(b-a)

	

def main ():
	print("simple trapezium!")
	print(trapezium(Cos,1,3))
	print(trapezium(Sqrt,2,10))
	print(trapezium(f1,-1,1))
	print(trapezium(f2,0,1))
	print(trapezium(Sin,2,7))
	print(trapezium(Cosh,0,1))
	print(trapezium(Sinh,0,2))
	print(trapezium(exp,-10,1))
	print(trapezium(lnoneminus,0.2,0.6))
	

#print(sys.argv)
if __name__ =='__main__': 
	main()


