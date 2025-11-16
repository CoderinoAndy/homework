# Lesson 28
def palindrome_checkera(a_str):
    return a_str[::-1] == a_str
# Obviously easier

def palindrome_checkerb(a_str):
    i = 0
    j = len(a_str) - 1
    reconstructed = ""
    for i in range(len(a_str)//2):
        if a_str[i] == a_str[j]:
            j -= 1
            continue
        else:
            return False
    return True
# Harder

# Efficiency wise if I were to guess its probably about the same? Depends on the big O of slicing backward

print(palindrome_checkera("tacocat"))
print(palindrome_checkerb("tacocat"))