# Lesson 21
n = int(input())

championfactors = 0
champion = 0

for number in range(1, n + 1):

    factors = 0

    for factor in range(1, number + 1):
        if number % factor == 0:
            factors += 1

    if factors > championfactors:
        champion = number
        championfactors = factors

print(champion)