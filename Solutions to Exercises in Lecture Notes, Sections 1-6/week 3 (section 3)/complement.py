""" complement_1.py
    Function computing complements of sets
    Author: Sergi Simon
    Last update: October 26, 2020 """


def complement ( smallerset, largerset ):
 	if smallerset.issubset(largerset) == False:
 		print ("The first set is not an actual subset of the second one")
 		return 0
 	return largerset.difference( smallerset )

print (complement ({1,2,3},{1,2,3,4,5,"a"}) )
print (complement ({1,2,"a"},{1,2,3,4,5,"a"}) )
print (complement ({1,2,"a"},{1,2,3,4,5}) )