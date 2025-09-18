# Lesson 3
# The instructions are a little strange... The input must be a perfect square for its tiles to create a square.
# Thus we have to explicitly ask the user to enter a perfect square.

from math import sqrt

while True:
    num = int(input("Enter a perfect square: "))
    root = sqrt(num)
    if root.is_integer() == True: #Researched about how to check if a number is an integer, since sqrt(num) returns a float
        print(f"Side length of the square is {root}")
        break
    else:
        print("Please enter a real perfect square.")