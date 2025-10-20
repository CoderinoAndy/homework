# Lesson 24
longest_length = 0
champion = ""
while True:
    name = input("Name: ")
    length = len(name)
    
    if name.upper() == "X":
        break

    if length > longest_length:
        champion = name
        longest_length = length

print(f"{champion} has the longest length with {longest_length} letters.")