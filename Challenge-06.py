"""
Task: 

Write a program that takes a maximum two-digit (1-99) number from the user and finds the pronunciation of that number.
For example:
İnput:97
Output:NinetySeven
"""

# Solution:

def pronounce_number(number):
    if number < 1 or number > 99:
        return "Invalid input"
    
    ones = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"]
    tens = ["", "", "Twenty", "Thirty", "Fourty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]
    teens = ["Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen","Eighteen", "Nineteen"]

    if number < 10:
        return ones[number]
    elif number < 20:
        return teens[number-10]
    else:
        return tens[number//10] + ones[number%10]
    
# Test the function
sample_number = 97
print("Sample Number: ", sample_number)
print("Expected Result:", "NineySeven")
print("Result:", pronounce_number(sample_number))  

# User Input Case
given_number = int(input("Enter a number between 1 and 99: "))
print(pronounce_number(given_number))
