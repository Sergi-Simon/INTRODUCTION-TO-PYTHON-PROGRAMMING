""" modifytable.py
	Program modifying the file previously built by table.py
	Author: Sergi Simon
	Last update: November 25, 2020 """

inp = input( "choose which method you prefer: a or r+" )
k = int( input( "print k") )
string = "{}_rows.txt".format(k)

if inp == "a":   
    file=open(string,"a")
    x = -1
    file.write( f"\n{1} \t {x:.16f}" )
    for i in range ( 1, k ):
        x /= -2
        file.write( f"\n{i+1} \t {x:.16f}" )
    file.close()
if inp == "r+":
    file=open(string,"r+")
    lines = file.readlines( )
    for i in range( k ):
        values = lines[i].split()
        file.write( f"\n{int(values[0])} \t {-1/float(values[1]):.16f}" )
    file.close()