""" characterlist.py
	Program receiving a string and returning a double list
    collating each character against the frequency with which it occurs in the string
	Author: Sergi Simon
	Last update: November 4, 2020 """

sentence = input("Write a sentence: ")
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

list1 = []
for letter in alphabet: 
    times = 0
    for sletter in sentence: 
        if sletter == letter:
            times += 1
    if times > 0 :
        list1.append( [ letter, times ] )    

print( list1 )