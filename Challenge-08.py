"""
Task: 

Let's solve questions on creating different pyramid shapes
Program to print half pyramid a using numbers.(User enter the numbers of rows)
"""

# Solution:

# Half Pyramid
def halfPyramid(rows):
    for i in range(1, rows + 1):
        for j in range(1, i + 1):
            print(j, end=" ")
        print("\n")

# Given Case
rows = int(input("Enter the number of rows: "))
print("Half Pyramid")
halfPyramid(rows)
