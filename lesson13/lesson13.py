# Lesson 13
month = int(input())
day = int(input())
if (month, day) == (2, 18):
    print("Special")
elif (month, day) < (2, 18):
    print("Before")
else:
    print("After")