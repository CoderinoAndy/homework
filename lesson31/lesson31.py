# Lesson 31
def anagram(stringie_a, stringie_b):
    list_a = list(stringie_a.replace(" ", ""))
    list_b = list(stringie_b.replace(" ", ""))

    if len(list_a) != len(list_b):
        return False

    switched = True
    length = len(list_a)
    while switched:
        switched = False
        for x in range(1, length):
            if list_a[x - 1] > list_a[x]:
                list_a[x - 1], list_a[x] = list_a[x], list_a[x - 1]
                switched = True
    switched = True
    while switched:
        switched = False
        for x in range(1, length):
            if list_b[x - 1] > list_b[x]:
                list_b[x - 1], list_b[x] = list_b[x], list_b[x - 1]
                switched = True
    return list_a == list_b
print(anagram("Justi2n", "inJ ust3"))

# Holy bubble sort