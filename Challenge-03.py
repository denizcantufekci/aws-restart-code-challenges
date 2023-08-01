"""
Task: 

Write a Python program to get a string from a given string where all occurrences of its first char have been changed to '$', except the first char itself.
Sample String : 'restart
Expected Result : 'resta$t
"""

# Solution:

def replace_first_repeated(input_string):
    
    #if an empty string is passed, return an empty string
    if not input_string:
        return ""

    char_count = {}
    first_replaced_char = ""
    char_replaced = True
    result_string = input_string
    index = 0

    for char in input_string:
        index += 1

        if char in char_count:
            char_count[char] += 1
            
            if char_count[char] > 1:
                if char_replaced:
                    first_replaced_char = char
                    char_replaced = False

            if first_replaced_char == char:
                result_string = result_string[:index-1] + '$' + result_string[index:]

        else:
            char_count[char] = 1

    return result_string

# Test the function
sample_string = 'rressstttaarrrtt'
result = replace_first_repeated(sample_string)
print("Sample String:", sample_string)
print("Expected Result:", "r$essstttaa$$$tt")
print("Result:", result)

# User Input Case
given_string = input("Enter a string: ")
print(replace_first_repeated(given_string))

"""
# Instructor's Solution
text = input("")
text = text[0] + text[1:].replace(text[0], "$")
print(text)
"""