""" primedecomposition.py
	Program asking for a number and returning its prime decomposition
	Author: Sergi Simon
	Last update: November 28, 2020 """


def try_prime( n ):
	i = 2
	while n % i != 0:
		i+=1
	if i == n:
		return True
	return False

# the slow version
def list_primes1( n ):
	list1=[]
	for i in range (2,n+1):
		if try_prime(i)== True:
			list1.append(i)
	return list1

# the fast version
def list_primes2( n ):
	list1 = list(range(2, n+1))
	for i in range(len(list1)):
		for j in range(i+1,len(list1)):
			if list1[i]!=0 and list1[j]!=0:
				if list1[j] % list1[i] ==0:
					list1[j]=0
	
	list1.sort()
	while list1[0]==0:
		list1.pop(0)
		
	return list1



def prime_decomposition( n ):
	if try_prime(n) == True:
		return [n]
	list1=list_primes2(n)
	list2=[]
	k = n
	while len(list1)>0:
		x=list1[0]
		while k%x ==0:
			list2.append(x)
			k=k//x
		list1.pop(0)

	return list2


n = int(input("Write a positive integer larger than 2: "))
print(prime_decomposition(n))
