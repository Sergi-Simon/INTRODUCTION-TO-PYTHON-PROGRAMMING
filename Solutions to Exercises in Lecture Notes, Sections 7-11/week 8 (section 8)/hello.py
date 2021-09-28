def main( ):
    print( "hello!")

def sum ( a, b ):
    return a+b

if __name__ == "__main__":
    main( )

if __name__ == "hello":
    print( "this program", __name__ , " is being run from an external source")

print( "and goodbye")
print( sum ( 2, 4 ) )