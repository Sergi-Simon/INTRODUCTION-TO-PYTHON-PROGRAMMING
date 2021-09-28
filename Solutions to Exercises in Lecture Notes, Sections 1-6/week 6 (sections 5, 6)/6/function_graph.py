""" 	function_graph.py
	Routine that checks the number of changes in sign in the graph provided in the lecture notes
	Author: Sergi Simon
	Last Update: November 18, 2020 """
import sys

def verify_signs ( x0, x1 ):
	if x0 == -3 or x0 == 2 or x0 == 6 or x1 == -3 or x1 == 2 or x1 == 6:
		string = "you have chosen interval limits, please choose other numbers"
#	elif x0 >= x1: 
#		string = "please write numbers such that the first is smaller than the second"
	elif x0 < -3:
		if x1 < -3: 
			string = "zero changes in sign"
		elif x1 < 2:
			string = "one change in sign"
		elif x1 < 6: 
			string = "two changes in sign"
		else:
			string = "three changes in sign"
	elif x0 < 2:
		if x1 < 2: 
			string = "zero changes in sign"
		elif x1 < 6: 
			string = "one change in sign"
		else: 
			string = "two changes in sign"
	elif x0 < 6:
		if x1 < 6: 
			string = "zero changes in sign"
		else: 
			string = "one change in sign"
	else: 
		string = "zero changes in sign"		
	
	return string

def inputx0x1( ):
    global x0, x1
    try: 
        print( "Write x0 and x1")
        x0 = float( input("x0 = ") )
        x1 = float( input("x1 = ") )
        
        if x0 >= x1:
            raise Exception ('numbers but not in the right order')                 
    except ValueError:
        print( 'They need to be numbers!')
    except Exception as inst:
        print( 'These are ', inst )
    else:
        print( 'We have your two values properly stored')
        return True
        
while True:
    if( inputx0x1() ):
        print(verify_signs(x0,x1))
        break
    else:
        print( "try proper x0, x1" )




