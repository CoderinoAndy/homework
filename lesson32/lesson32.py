# Lesson 32
def sharedchar(string1, string2):
    final = []
    combined = list(string1) + list(string2)
    for x in combined:
        if x not in final:
            final.append(x)
    swapped = True
    while swapped:
        swapped = False
        for i in range(1, len(final) - 1):
            if final[i - 1] > final[i]:
                final[i - 1], final[i] = final[i], final[i - 1]
                swapped = True
    return final
print(sharedchar("final", "jima"))        
        

    

            

