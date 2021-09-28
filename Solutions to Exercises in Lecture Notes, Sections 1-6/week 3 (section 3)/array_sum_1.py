""" array_sum_1.py
    Recursive function adding arrays 
    Author: Sergi Simon
    Last update: October 26, 2020 """

def add_array ( array1, array2 ):
	# We check the validity of our inputs
	if type(array1)!=type(array2):
		print("They should have the same type")
		return 0
	if type(array1) != tuple:
		if type (array1) != list:
			print ("Your inputs are neither tuples nor lists")
			return -1
	
	list1 = array1
	if type( array1 ) == tuple:
		list1 = list ( array1 )

	list2 = array2
	if type( array2 ) == tuple:
		list2 = list ( array2 )

	# add
	result = add_list(list1,list2)

	# convert if necessary
	if type( array1 ) == tuple:
		result = tuple(result)

	return result

# recursive function adding arrays
def add_list ( list1, list2 ):
	if list1==[]:
		return []
	aux=[list1[0]+list2[0]]
	return aux+add_list ( list1[1:], list2[1:] )




print ( add_array ( (1,2,3), (5,6,7) ))
print ( add_array ( (0.2,2.4,1.1), (-5,6.7,9.9) ))
print ( add_array ( [0.2,2.4,1.1], [-5,6.7,9.9] ))