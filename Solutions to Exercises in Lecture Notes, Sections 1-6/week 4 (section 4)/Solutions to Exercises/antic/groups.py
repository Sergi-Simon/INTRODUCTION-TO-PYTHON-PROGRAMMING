""" groups.py
	Program using dictionaries to process groups of people
	Author: Sergi Simon
	Last Update: October 12, 2019 """


person1 = {
	"name" : "Jane", 
	"age" : 23, 
	"birthday": {
		"month": 12,
		"day": 27
	}
}

person2 = {
	"name" : "John", 
	"age" : 24, 
	"birthday": {
		"month": 11,
		"day": 20
	}
}


person3 = {
	"name" : "Mary", 
	"age" : 22, 
	"birthday": {
		"month": 8,
		"day": 10
	}
}


person4 = {
	"name" : "Peter", 
	"age" : 12, 
	"birthday": {
		"month": 8,
		"day": 1
	}
}


person5 = {
	"name" : "Peter", 
	"age" : 8, 
	"birthday": {
		"month": 9,
		"day": 2
	}
}



group = {
	"person1" : person1, 
	"person2" : person2, 
	"person3" : person3, 
	"person4" : person4, 
	"person5" : person5 
}


print( " First part of the exercise ")
Key = input( " write the key you're interested in ")

listofkeys=[]
for x in group.keys(): 
	if not ( Key in group[x].keys() ):
		print ( str(x)+" having name "+str(group[x]["name"])+" does not have this Key")
		break
	listofkeys.append(group[x][Key])
print( listofkeys )



print ("Second part of the exercise")
age = int(input("write the age"))
ageequal = False
for x in group.keys():
	if group[x]["age"] == age:
		savekey = x
		ageequal = True
		break
if ageequal == True:
	print ("we found a person with this age: "+str(group[x]["name"]))
if ageequal == False:	
	print ("we found nobody with this age")



print ("Third part of the exercise")	
age = int(input("write the threshold age"))
kiddies_table={}
i=1
for x in group.keys():
	if group[x]["age"] < age:
		string ="kid"+str(i)
		kiddies_table[string]=group[x]
		i += 1
print(kiddies_table)
