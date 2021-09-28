""" sum_1.py
	Function computing the sum \sum_{k=0}^n 1/k^2
	Author: Sergi Simon
	Last update: October 28, 2020 """

def sum_of_terms ( k ):
	s = 0.
	for i in range (k):
		i1 = i+1
		s += 1./(i1*i1)
	return s

k = int(input( "Write the number of summands you want: "))
print ("The sum is "+str(sum_of_terms(k)))
