"""
Task: 

Write a Python program to get a string made of the first 2 and the last 2 chars from a given a string. 
If the string length is less than 2, return instead of the empty string.
"""

# Solution:

def get_specific_chars(input_string):
        
        if not input_string:
            return ""
        if len(input_string) < 2:
            return ""
        
        first_two_chars = input_string[:2]
        last_two_chars = input_string[-2:]

        return first_two_chars + last_two_chars

# Test the function
sample_string = "Empty String"
result = get_specific_chars(sample_string)
print("Sample String 1: ", sample_string)
print("Expected Result 1:", result)

sample_string = ""
result = get_specific_chars(sample_string)
print("Sample String 2: ", sample_string)
print("Expected Result 2:", result)

sample_string = "A"
result = get_specific_chars(sample_string)
print("Sample String 3: ", sample_string)
print("Expected Result 3:", result)

sample_string = "AW"
result = get_specific_chars(sample_string)
print("Sample String 4: ", sample_string)
print("Expected Result 4:", result)

sample_string = "AWS"
result = get_specific_chars(sample_string)
print("Sample String 5: ", sample_string)
print("Expected Result 5:", result)

# User Input Case
given_string = input("Enter a string: ")
print(get_specific_chars(given_string))

"""
# Instructor's Solution
text = input("")
if len(text) < 2 :
  word = "Empty String"
else :
  word = text[0:2] + text[-2:]
print(word)
"""