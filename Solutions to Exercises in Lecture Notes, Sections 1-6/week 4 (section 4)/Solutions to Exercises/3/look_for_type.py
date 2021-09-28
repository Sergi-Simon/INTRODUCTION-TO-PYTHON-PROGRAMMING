""" look_for_type.py
	Function looking for a given type in an array
	Author: Sergi Simon
	Last update: October 28, 2020 """

def look ( array, _type ):
	index = -1
	for i in range(len(array)):
		if type(array[i])==_type:
			index = i
			break
	return index

print( look( [0,1,2,3,1,0.1, "a",2], str) )
print( look( [0,1,2,3,1,0.1, "a",2,0.5], int) )
print( look( [0,1,2,3,1,0.1, "a",2], float) )