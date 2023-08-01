"""
Task: Write a Python program to sum of three given integers. However, if two values are equal sum will be zero.
"""

# Solution:

# User Input Case
value1 = int(input("Enter first number: "))
value2 = int(input("Enter second number: "))
value3 = int(input("Enter third number: "))

# Sum of three given integers
if (value1 != value2 and value2 != value3 and value1 != value3):
    print('Sum of', value1, '+', value2, '+', value3, '=', value1 + value2 + value3)
else:
    print('Sum is zero!')

"""
# Instructor's Solution
num1 = (input("birinci sayiyi girin :"))
num2 = (input("ikinci  sayiyi girin :"))
num3 = (input("üçüncü sayiyi girin : "))

if num1 == num2 or num1 == num3 or num2 == num3 :
  print(0)
else:
  print(num1 + num2 + num3)
"""