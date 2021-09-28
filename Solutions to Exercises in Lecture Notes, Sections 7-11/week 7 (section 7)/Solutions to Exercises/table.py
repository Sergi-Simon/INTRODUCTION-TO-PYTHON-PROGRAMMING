"""
table.py

author: 
last update: 24-11-2020 
program taking an integer k by keyboard input and 
creating an external file k_rows.txt wherein it writes k rows:

1   1.000
2   -2.000
3   4.000
4   -8.000
....

"""

while True:
    try:
        k = int( input( "write k " ) )
        if k <= 0:
            raise ValueError
        break
    except:
            print( "please use a proper number ")

if k == 1:
    filename = f"{k}_row.txt"
else:
    filename = f"{k}_rows.txt"

myfile = open( filename, "w" )

x = 1
myfile.write( f"{1} \t {x:.3f}" )
for i in range ( 1, k ):
    x *= -2
    myfile.write( f"\n{i+1} \t {x:.3f}" )


myfile.close()