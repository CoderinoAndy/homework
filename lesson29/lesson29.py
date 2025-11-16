# Lesson 29
def consocount(string_cheese):
    vowels = "AEIOU"
    count = 0
    for character in string_cheese:
        if character.isalpha() and character not in vowels:
            count += 1
    return count

print(consocount("H 1 E 2 L 3"))