# Lesson 33
mylist = []
amountToAdd = int(input("amount to add: "))
for x in range(amountToAdd):
    toadd = int(input("What to add: "))
    mylist.append(toadd)

# finding the mean
def mean(listy):
    total = 0
    count = 0
    for x in mylist:
        count += 1
        total += x
    return total/count

def median(listy):
    swapped = True
    while swapped:
        swapped = False
        for x in range(1, len(listy)):
            if listy[x - 1] > listy[x]:
                listy[x - 1], listy[x] = listy[x], listy[x - 1]
                swapped = True
    if len(listy) % 2 == 0:
        return (listy[len(listy)//2 - 1] + listy[len(listy)//2])/2
    else:
        return listy[len(listy)//2]

print(mean(mylist))
print(median(mylist))