""" remove.py
	Function removing all occurrences of a given member
	Author: Sergi Simon
	Last Update: November 3, 2020 """

def remove_all( array, member ):
	if type( array ) == list:
		list1 = array.copy()
		result = remove_from_list( list1, member )
	if type ( array ) == tuple: 
		list1 = list( array )
		result = tuple( remove_from_list( list1, member ) )
	if type ( array ) == set:
		result = array.copy()
		result.remove( member )
    # remember: we haven't seen dictionaries this year!
	if type ( array ) == dict:
		result = array.copy()
		del result[str(member)]
	return result


# recursive version
def remove_from_list_recursive( list1, member ):
    if list1==[]:
        return []
    aux = [list1[0]]
    if list1[0]==member:
        aux.remove(member)
        # in which case aux==[]
    return aux[:1]+remove_all(list1[1:],member)

# non-recursive version
def remove_from_list( list1, member ):
    if list1==[]:
        return []
    list2 = list1.copy()
    i = 0
    while i < len( list2 ):
        if list2[i]==member:
            list2.pop(i)
        i +=1
       
    return list2

    
print (remove_all([0,1,2],2))

# remember: we haven't seen dictionaries this year!
person1 = {
	"name" : "Jane", 
	"age" : 23, 
	"birthday": {
		"month": 12,
		"day": 27
	}
}
print (remove_all(person1,"name"))


print (remove_all((0,"a",1,"a",3),"a"))
print (remove_all({1,2,"hello"},2))