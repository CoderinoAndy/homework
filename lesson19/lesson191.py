# lesson 19 1.0
def prime_getter(number):
    if number <= 1:
        return False
    if number == 2:
        return True

    factor = 2

    while factor < number:
        if number % factor == 0:
            return False
        else:
            factor += 1
            continue
    
    return True

n = int(input("number: "))

if prime_getter(n):
    print(f"{n} is prime.")
else:
    print(f"{n} is not prime.")
