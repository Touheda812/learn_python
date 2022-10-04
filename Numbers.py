'''
Operators: + , - , * , /, // , %
Data Types: int, float, string
Numerica Types: int, float, complex
Division (/) which returns float but Floor Division (//) returns integer discarding any fractional result
Multiplication (*)
squared (**) / pow(x,y)
how to round to 2 decimal point: round(variable,2)
divmod(quotient,reminder)
abs(x): absolute value
complex numbers: complex([real[,imag]])
Decimal
'''

# Floor division(//) vs division(/)
print('division:', 8 / 3)
print('floor division:', 8 // 3)

# pow(x,y) / Squared(x ** y) vs multiplication(x * y)
print("to the power of/squared:", pow(2, 3))
print(2 ** 3)
print('multiplication', 2 * 3)

# round(variable,2)
num_round = 2 * 3.4213
print('round number:', num_round)
print(round(num_round, 2))

# divmod (x,y)
'''divmod() returns (quotient,reminder) - a tuple that contains quotient and reminder of the division'''
print(10 // 3, 10 % 3)
result = divmod(10, 3)
print('divmod:', result)

# abs(x) - absolute value or magnitude of x
print('absolute value:', abs(-4.2 * 2))

# complex([real[,img]]) takes 2 parameters a)real b) imag
z = complex(2, -3)
print('Complex():', z)
z1 = complex(1)
print(z1)

# Decimal module
x = 0.1
y = 0.1
z = 0.1
s = x + y + z
print('Decimal:',s)

# Round Decimals
from decimal import Decimal
x = Decimal('0.1')
y = Decimal('0.1')
z = Decimal('0.1')
s = x + y + z
print('rounded decimal:',s)