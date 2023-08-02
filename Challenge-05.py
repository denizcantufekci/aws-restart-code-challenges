"""
Task: 

Write a Python program to display the examination schedule. (extract the date from exam_st_date)

exam_st_date = (11, 12, 2014)
Sample Output : The examination will start from : 11 / 12 / 2014
"""

# Solution:

def reproduceDate(inputDate):
    outputDate = inputDate.replace("(", "").replace(")", "")
    
    return outputDate.replace(", ", " / ")

# Given Case
Sample_date = str((11, 12, 2014))
print("Sample date: (11, 12, 2014)")
print("Expected Output: 11 / 12 / 2014")
print("Sample Result: ", reproduceDate(Sample_date))

# User Input Case
user_date = str(input("Please enter a date in the format (DD, MM, YYYY): "))
print("Sample Result: ", reproduceDate(user_date))
