# Lesson 25

def prime_factor_finder(num):
    factors = []
    prime_factors = []
    for factor in range(2, num + 1):
        if num % factor == 0:
            factors.append(factor)
    
    inner_factor = 1
    for factor in factors:
        is_prime = True
        inner_factor = 2
        while is_prime and inner_factor < factor:
            if factor % inner_factor == 0:
                is_prime = False
            inner_factor += 1
       
        if is_prime:
            prime_factors.append(factor)

    if prime_factors:
        return max(prime_factors)
    else:
        return None

n = int(input("Num: "))
print(prime_factor_finder(n))
    

