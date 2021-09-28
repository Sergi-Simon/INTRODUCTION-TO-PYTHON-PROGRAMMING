""" modifytable2.py
	Program modifying the file for the second time (to be run only after table.py and modifytable.py)
	Author: Sergi Simon
	Last update: November 25, 2020 """



k = int( input( "print k") )
string = "{}_rows.txt".format(k)
file=open(string,"r+")
f=file.readlines()
file.write("\n")
for i in range(k):
	line1 = (f[i]+f[i+k]).split()
	line1 = "\t".join(line1)+"\n"
	file.write(line1)
file.close()