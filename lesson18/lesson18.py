# Lesson 18
def factor_getter(number):
    for factor in range(1, number + 1):
        if number % factor == 0:
            print(factor)

n = int(input("what is your number: "))

factor_getter(n)
