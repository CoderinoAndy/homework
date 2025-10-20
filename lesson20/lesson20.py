# Lesson 20
for number in range(1, 10000):

    total = 0

    for factor in range(1, number):
        if number % factor == 0:
            total += factor

    if number == total:
        print(f"{number} is a perfect number.")


