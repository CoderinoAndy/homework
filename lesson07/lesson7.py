# Lesson 7
from random import randrange

difficulty_class = int(input("What is the difficulty class? "))
action = input("What is the action being attempted? ")
roll = randrange(1, 21) 
print(f"rolled: {roll}")
print(f"DC: {difficulty_class}")
if roll >= difficulty_class:
    print(f"Success! Your character is able to {action}.")
else:
    print(f"Fail... Your character was not able to {action}.")

