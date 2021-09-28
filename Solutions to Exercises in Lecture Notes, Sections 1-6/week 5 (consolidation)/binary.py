""" binary.py
	Program converting a number from decimal to binary and viceversa
	Author: Sergi Simon
	Last update: November 4, 2020 """
	
def to_decimal(n): #example of function using the input as a local variable
    n = list(n)
    n.reverse()
    decimal = 0
    for i in range(len(n)):
        decimal += int(n[i]) * 2 ** i
    return decimal

def to_binary(n): #example of function using the input as a local variable
    binary = []
    while n > 0:
        binary.append(str(n % 2))
        n //= 2
    binary.reverse()
    return ''.join(binary)

print(to_decimal('11110'))
print(to_binary(30))
print(to_decimal(to_binary(28)))
print(to_binary(to_decimal('111010')))