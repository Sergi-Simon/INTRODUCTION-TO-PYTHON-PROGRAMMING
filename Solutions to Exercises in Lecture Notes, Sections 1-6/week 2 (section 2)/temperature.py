""" temperature.py
    Prorgram that converts any temoerature from Fahrenheit to Celsius and
    from Celsius to Fahrenheit
    Author: Sergi Simon
    Last update: October 22, 2020 """

# conversion of Celsius to Fahrenheit
def C_to_F ( c ):
    return c*1.8 + 32.

# conversion of Fahrenheit to Celsius
def F_to_C ( f ):
    x=f-32.
    return x/1.8

# we give the option 
opt = input("Would you like to convert \n 1 Celsius to Fahrenheit or \n 2 Fahrenheit to Celsius?")
if opt == "1":
    c = float(input("Write the temperature in degrees Celsius "))
    f = C_to_F( c )
    print("The temperature in degrees Fahrenheit is ",f)
if opt == "2":
    f = float(input("Write the temperature in degrees Fahrenheit "))
    c = F_to_C( f )
    print("The temperature in degrees Celsius is ",c)
    
