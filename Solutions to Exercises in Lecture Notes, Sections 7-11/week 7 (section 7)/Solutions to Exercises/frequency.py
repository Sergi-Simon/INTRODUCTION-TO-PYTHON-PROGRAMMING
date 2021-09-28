""" frequency.py
	Program retrieving text from a file and performing a frequency analysis of its characters
	Author: Sergi Simon
	Last update: November 18, 2020 """

file = open( "text.txt", "r" )
u = file.read().lower()

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

list1 = []
for letter in alphabet: 
    times = 0
    for sletter in u: 
        if sletter == letter:
            times += 1
    
    if len( list1 ) == 0:
    	list1.append( [ letter, times ] )
    else:
    	for i in range(	len(list1)):
    		if list1[i][1] >= times:
    			list1.insert( i, [ letter, times ] )
    			break
    	if list1[-1][1] < times:
    		list1.append( [ letter, times ] )
list1.reverse()
print( list1 )


file.close()