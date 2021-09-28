""" password.py
	Program asking the user for a sentence and a character, then returning the number of times the character appears in the sentence
	Author: Sergi Simon
	Last update: November 4, 2020 """
    
key = "maryhadalittlelamb"
password =""
while password != key:
    password = input("Write the password: ")
print("Password is correct")