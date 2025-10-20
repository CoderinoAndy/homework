# Lesson 22
def fibo(num):
    # Location starts at 0
    if num in [0, 1]:
        return num
    else:
        first_back = 1
        second_back = 0
        location = 2
        while location <= num:
            current = first_back + second_back
            second_back = first_back
            first_back = current
            location += 1
        return current

print(fibo(10))