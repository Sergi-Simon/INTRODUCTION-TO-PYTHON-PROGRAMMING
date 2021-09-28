""" subjects.py
	Program using a list to store subjects
	Author: Sergi Simon
	Last update: October 28, 2020 """


subjects = ["Maths", "Physics", "Chemistry", "Statistics", "Whatever"]
passed = []
for subject in subjects:
    score = float(input("What marks did you get in " + subject + "?"))
    if score >= 40:
        passed.append(subject)
for subject in passed:
    subjects.remove(subject)
if len(subjects ) ==0:
	print("You must repeat none" )
if len(subjects ) >0:
	print("You must repeat " + str(subjects))



