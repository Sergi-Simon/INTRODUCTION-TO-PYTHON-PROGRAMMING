def factorial (n):
	if n==0:
		return 1
	return n*factorial(n-1)


def Cos ( A, *args ):
	s = 0
	n=25
	a = float(A)
	if len(args)>0:
		n = args[0]
	for k in range (n):
		var = 2*k
		s += (-1)**k *(a**var) / factorial(var)
	return s

def Sin ( A, *args ):
	s = 0
	n=25
	a = float(A)
	if len(args)>0:
		n = args[0]
	for k in range (n):
		var = 2*k+1
		s += (-1)**k *(a**var) / factorial(var)
	return s

def Cosh ( A, *args ):
	s = 0
	n=25
	a = float(A)
	if len(args)>0:
		n = args[0]
	for k in range (n):
		var = 2*k
		s += (a**var) / factorial(var)
	return s

def Sinh ( A, *args ):
	s = 0
	n=80
	a = float(A)
	if len(args)>0:
		n = args[0]
	for k in range (n):
		var = 2*k+1
		s += (a**var) / factorial(var)
	return s

def exp ( A, *args ):
	s = 0
	n=80
	a = float(A)
	if len(args)>0:
		n = args[0]
	for k in range (n):
		s += (a**k) / factorial(k)
	return s

def lnoneminus ( A, *args ):
	s = 0
	n=80
	a = float(A)
	if len(args)>0:
		n = args[0]
	for k in range (1,n):
		s += (a**k) / (k)
	return -s
