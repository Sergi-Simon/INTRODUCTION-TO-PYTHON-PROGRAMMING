""" vowel.py
	program taking a character and returning True if it is a vowel, and False otherwise.
	Author: Sergi Simon
	Last Update: November 4, 2020 """

def vowel ( string ):
	for x in string:
		if x == 'a' or x == 'e' or x == 'i' or x == 'o' or x == 'u':
			return True
		if x == 'A' or x == 'E' or x == 'I' or x == 'O' or x == 'U':
			return True
	return False

string = input("write a string")
var = vowel(string)
if var:
	print ("The string has at least a vowel")
else:
	print ("The string has no vowels")