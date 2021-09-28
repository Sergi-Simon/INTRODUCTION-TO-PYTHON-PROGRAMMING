""" replace_array_2.py
    Non-recursive functions replacing elements in arrays 
    Author: Sergi Simon
    Last update: October 28, 2020 """


# this is the same as in the older file
def replace_array_index ( array1, index1, newvalue ):
	# We check the validity of our inputs
	if type(array1) != tuple:
		if type (array1) != list:
			print ("Your first input is neither a tuple nor a list")
			return 0
	if index1 < 0:
		print ("Your index is negative")
		return -1
	if index1 >= len(array1):
		print ("Your index is too large")
		return -2

	# We make sure we can modify our working array
	list1 = array1
	if type( array1 ) == tuple:
		list1 = list ( array1 )

	# We modify it
	list1[index1]=newvalue

	# we prepare the return
	result = list1

	# convert if necessary
	if type( array1 ) == tuple:
		result = tuple(result)

	return result




# THIS ONE IS NEW
def replace_array_value ( array1, value, newvalue ):
	# We check the validity of our inputs
	if type(array1) != tuple:
		if type (array1) != list:
			print ("Your inputs are neither tuples nor lists")
			return 0
	
	list1 = array1
	if type( array1 ) == tuple:
		list1 = list ( array1 )
		

	# method 1: we use in
	if not (value in array1):
		print ("The element is not in the array! checked using in")
		return -1
	# method 2: we use list.count()
	if list1.count(value)==0:
		print ("The element is not in the array! checked using list.count")
		return -1
	# method 3: we use len
	list2=list1.copy()
	list2.remove(value)
	if len(list1) == len(list2):
		print ("The element is not in the array! checked using len")
		return -1


	# replace
	for i in range(len(list1)):
		if list1[i]==value:
			list1[i]=newvalue 
	
	# convert if necessary
	result = list1
	if type( array1 ) == tuple:
		result = tuple(result)

	return result

# recursive function replacing elements in a list
def replace_list_value ( list_1, value, newvalue ):
	if list_1==[]:
		return list_1
	aux=[list_1[0]]
	if list_1[0]==value:
		aux=[newvalue]
	return aux[:1]+replace_list_value ( list_1[1:], value, newvalue )

def swap_array_indices ( array1, index1, index2 ):
	# We check the validity of our inputs
	if type(array1) != tuple:
		if type (array1) != list:
			print ("Your first input is neither a tuple nor a list")
			return 0
	if index1 < 0:
		print ("Your first index is negative")
		return -1
	if index1 >= len(array1):
		print ("Your first index is too large")
		return -2
	if index2 < 0:
		print ("Your second index is negative")
		return -1
	if index2 >= len(array1):
		print ("Your second index is too large")
		return -2

	list1 = array1
	if type( array1 ) == tuple:
		list1 = list ( array1 )

	aux = list1[index1]
	list1[index1] = list1[index2]
	list1[index2] = aux

	# we prepare the return
	result = list1

	# convert if necessary
	if type( array1 ) == tuple:
		result = tuple(result)

	return result

	


print ( replace_array_index ( (1,2,"a"), 2, "aa" ))
print ( replace_array_index ( [1,0.1,"a","b",1], 4, 2 ))
print ( replace_array_value ( [1,0.1,"a","b",1], 0.1, 0.2 ))
print ( replace_array_value ( (1,0.1,"a","b",1,3,4,5,6,4,5,6), 4, "c" ))
print ( replace_array_value ( [1,0.1,"a","b",1,3,4,5,6,4,5,6,0,1], 4, "c" ))
print ( swap_array_indices ( [1,0.1,"a","b",1,3,4,5,6,4,5,6,0,1], 0, 1 ) )
print ( swap_array_indices ( [1,0.1,"a","b",1,3,4,5,6,4,5,6,0,1], 4, 7 ) )
print ( swap_array_indices ( (1,0.1,"a","b",1,3,4,5,6,4,5,6,0,1,3,4,5), 5, 8 ) )
print ( swap_array_indices ( [1,0.1,"a","b",1,3,4,5,6,4,5,6,0,1], -1, 7 ) )
print ( swap_array_indices ( (1,0.1,"a","b",1,3,4,5,6,4,5,6,0,1,3,4,5), 5, 18 ) )

