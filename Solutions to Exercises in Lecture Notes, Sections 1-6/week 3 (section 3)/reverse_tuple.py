""" reverse_tuple.py
    Function that reverses any tuple
    Author: Sergi Simon
    Last update: October 26, 2020 """

def reverse_tuple ( Tuple ):
    list1 = list( Tuple )
    list1.reverse()
    return tuple( list1 ) 

print( reverse_tuple( (1,2,3) ) )
x= 1,2,3,"a","good morning", -1,-2
print( reverse_tuple( x ) )
