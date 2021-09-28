import functions as fun 


print( "this is the main program ")
print( "__name__ is", __name__ )

def main():
    print( "main function in main program ")
if __name__ == "__main__":
    main( )
    
def reminder ( ):
    print( "this is a function defined in the main program")
    
print( fun.f (2 ))