""" email_input.py
    Function testing the validity of an email address
    Author: Sergi Simon
    Last update: October 28, 2020 """


def email_process ( email ):
	# we count @
	atcount = 0
	for i in range(len(email)):
		if email[i] == "@":
			indexat = i
			atcount += 1
	# if no ats or more than one are counted
	if atcount != 1:
		return -1
	# if there is no character left of the at
	if indexat == 0:
		return -2
	# if there is no character right of the at
	if indexat == len(email)-1:
		return -3	

	# we count dots
	dotcount=0
	for i in range(indexat+1,len(email)):
		if email[i]==".":
			dotcount+= 1
	if dotcount ==0:
		return -4
	return 0

email = input( "print the email")
k = email_process(email)
if k==0:
	print("your email seems ok")
if k==-1:
	print("your email does not have exactly one @ and thus is not ok")	
if k==-2:
	print("your email has nothing to the left of the @ and thus is not ok")	
if k==-3:
	print("your email has nothing to the right of the @ and thus is not ok")	
if k==-4:
	print("your email does not have at least one dot where it should and thus is not ok")		