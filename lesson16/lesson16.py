# Lesson 16
for number in range(1, 51):
    if number%5 == 0:
        print("Buzz")
        if number%3 == 0:
            print("FizzBuzz")
    elif number%3 == 0:
        print("Fizz")
    else:
        print(number)
