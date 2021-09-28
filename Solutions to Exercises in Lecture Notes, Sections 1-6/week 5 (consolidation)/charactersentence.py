""" charactersentence.py
	Program asking the user for a sentence and a character, then returning the number of times the character appears in the sentence
	Author: Sergi Simon
	Last update: November 4, 2020 """
    
    
    
    
sentence = input("Write a sentence: ")
character = input("Write a character")
counter = 0
for i in sentence:
    if i == character:
        counter += 1
# we use formatting in this print command; we will see this in a couple weeks
string = 'times'    
if counter == 1:
    string = 'time'

# we will see more about formatting 
print("Character '%s' appears %2i %s in the sentence '%s'." % (character, counter, string, sentence))