"""
Task: 

Write a program (using functions!) that asks the user for a long string containing multiple words. 
Print back to the user the same string, except with the words in backwards order. 

For example, say I type the string:
"My name is Michele"

Then I would see the string:
"Michele is name My"
Shown back to me.
"""

# Solution:

def reverseString(inputString):
    outputString = inputString.split()
    outputString.reverse()
    outputString = " ".join(outputString)
    return outputString

# Given Case
Sample_string = "My name is Michele"
print("Sample string: My name is Michele")
print("Expected Output: Michele is name My")
print("Sample Result: ", reverseString(Sample_string))

# User Input Case
user_string = str(input("Please enter a string: "))
print("Sample Result: ", reverseString(user_string))
