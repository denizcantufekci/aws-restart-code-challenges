"""
Write a Python program to compute the greatest common divisor (GCD) of two positive integers.
"""

# Task: Python program to find GCD of two numbers
# Solution:

# Function to return gcd of a and b
def gcd(a, b):
    if (a == 0):
        return b
    return gcd(b % a, a)

# User Input Case
value1 = int(input("Enter first number: "))
value2 = int(input("Enter second number: "))

# GCD is defined as the greatest common divisor of at least two positive integers.
# Zero is not a positive integer. So, we need to check if the user input is not zero.
if (value1 != 0 and value2 != 0):
    print('GCD of', value1, 'and', value2, 'is', gcd(value1, value2))
else:
    print('Greatest common divisor is not found!')

"""
# Instructor's Solution
num1 = int(input("please enter a number : "))
num2 = int(input("please enter a number : "))
if num1 > num2 :
  bolen =  num2
else:
  bolen = num1
for i in range(1,bolen+1):
  if num1 % i == 0 and num2 % i == 0 :
    total = i

print(total)
"""