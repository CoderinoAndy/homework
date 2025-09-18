# Lesson 7
from random import randrange

difficulty_class = int(input("What is the difficulty class? "))
action = input("What is the action being attempted? ")
# Fun little action inquiry, if the dungeon master wants more immersion. Of course, we can not ensure grammatical accuracy here...
roll = randrange(1, 21) 
# In further research, randrange isn't inclusive of the second argument. If I were to do 20, it would only select numbers equal
# to or below 19. randint() from random would be a better choice since it is inclusive, but in accordance to the lesson specifications
# I will use randrange with 21 as the second argument :)
print(f"rolled: {roll}")
print(f"DC: {difficulty_class}")
if roll >= difficulty_class:
    print(f"Success! Your character is able to {action}.")
else:
    print(f"Fail... Your character was not able to {action}.")

