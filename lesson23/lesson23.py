# Lesson 23

total = 0
counter = 0
average = 0

while True:
    num = input()
    if num == "exit":
        break
    else:
        total += int(num)
        counter += 1
    
average = total/counter
print(average)