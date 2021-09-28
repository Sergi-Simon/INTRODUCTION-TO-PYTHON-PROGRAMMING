""" is_palindrome.py
	function deciding whether a string is a palindrome
	Author: Sergi Simon 
	Last Update: November 4, 2020 """

def is_palindrome ( string ):
	n = len(string)
	for i in range(n):
		if string[i] != string[-i-1]:
			return False
	return True

string = input("Write a string")
var = is_palindrome(string)
if var:
	print ("The string is a palindrome")
else:
	print ("The string is not a palindrome")