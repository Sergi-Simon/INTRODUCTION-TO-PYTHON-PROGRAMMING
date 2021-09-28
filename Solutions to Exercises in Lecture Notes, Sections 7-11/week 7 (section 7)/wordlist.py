""" wordlist.py
	Program receiving a string and returning a double list
    collating each word against the frequency with which it occurs in the string
	Author: Sergi Simon
	Last update: November 18, 2020 """
    
sentence = input("Write a sentence: ")

Sentence = sentence.split()
Wordpool = []
for word in Sentence:
    if not( word in Wordpool ):
        Wordpool.append( word )
print( Wordpool )

list1 = []
for word1 in Wordpool: 
    times = 0
    for word2 in Sentence: 
        if word1 == word2:
            times += 1
    list1.append( [ word1, times ] )    

print( list1 )