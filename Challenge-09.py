"""
Task: 

Let's solve questions on creating different pyramid shapes
Program to print full pyramid a using numbers.(User enter the numbers of rows)
"""

# Solution:

# Full Pyramid
def fullPyramid(rows):
    for i in range(1, rows+1):
        print(" "*(rows-i), end="")
        for j in range(1, i+1):
            print(j, end=" ")
        print()

# Given Case
rows = int(input("Enter the number of rows: "))
print("Full Pyramid")
fullPyramid(rows)
