""" for_to_which.py
    Program converting the for loops into while loops
	Author: Sergi Simon
	Last Update: October 28, 2020 """

print ("first loop")
""" list1=[1, 3.4, "a"]
for x in list1:
	print (x)"""

list1=[1, 3.4, "a"]
i=0
while i<len(list1):
	print ( list1[i] )
	i += 1


print ("second loop")
""" list2=[1, 3.4, "a","b",-0.2,[1,2]]
for u in list2:
    if type(u)==str:
        print (u) """

list2=[1, 3.4, "a","b",-0.2,[1,2]]
i = 0
while i<len(list2):
	if type(list2[i])==str:
		print (list2[i])
	i+=1

print ("third loop")
"""tuple_1=1, 2, 3, 4, 10, 20, 30, 40 
for i in tuple_1:
   if i%3==1:
       print (i)"""

tuple_1=1, 2, 3, 4, 10, 20, 30, 40 
i = 0
while i<len(tuple_1):
   if tuple_1[i]%3==1:
       print (tuple_1[i])       
   i+=1
   
print ("fourth loop")
""" set_1={1,3,7,17}
for j in set_1:
	print (j//2)"""

set_1={1,3,7,17}
set_2 = set_1.copy()
while len(set_2)>0:
	j = max(set_2)
	print (j//2)
	set_2.remove(j)


print ("fifth loop")
"""for j in {1,2,"u"}:
	print ("hello") """

set_2={1,2,"u"}.copy()
while len(set_2)>0:
	print ("hello")	
	set_2.pop()

print ("sixth loop")
"""email = False
for i in "mymail@gmail.com":
    if i=="@":
        email = True
if email: # Another way of writing if email == True print("This seems to be an email address")"""

email = False
string = "mymail@gmail.com"
i = 0
while i < len(string):
    if string[i]=="@":
        email = True
        break
    i+=1
if email: # Another way of writing if email == True 
	print("This seems to be an email address")

# EXERCISE: you do the rest!
