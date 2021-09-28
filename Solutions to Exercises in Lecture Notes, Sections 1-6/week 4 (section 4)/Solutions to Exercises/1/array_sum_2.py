""" array_sum_2.py
    Function adding arrays with loops
    Author: Sergi Simon
    Last update: October 28, 2020 """

def add_array ( array1, array2 ):
	# We check the validity of our inputs
	if type(array1)!=type(array2):
		print("They should have the same type")
		return 0
	if type(array1) != tuple:
		if type (array1) != list:
			print ("Your inputs are neither tuples nor lists")
			return -1
	
	# we create lists containing the entries in our arguments
	list1 = array1
	if type( array1 ) == tuple:
		list1 = list ( array1 )

	list2 = array2
	if type( array2 ) == tuple:
		list2 = list ( array2 )

	# add the lists 
	result = add_list(list1,list2)

	# convert if necessary
	if type( array1 ) == tuple:
		result = tuple(result)

	return result

# recursive function adding arrays
def add_list ( list1, list2 ):
	list3 = []
	for i in range(len(list1)):
		list3.append(list1[i]+list2[i])
	return list3
		
print ( add_array ( (1,2,3), (5,6,7) ))
print ( add_array ( (0.2,2.4,1.1), (-5,6.7,9.9) ))
print ( add_array ( [0.2,2.4,1.1], [-5,6.7,9.9] ))