""" reverseword.py
	Program asking the user for a word, 
    then showing each of the characters of the word onscreen in reverse order
	Author: Sergi Simon
	Last update: November 4, 2020 """
    
word = input("Write a word: ")
for i in range(len(word)-1, -1, -1):
    print(word[i])    
