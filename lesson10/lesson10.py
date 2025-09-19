# Lesson 10
switch = True
number = input("Give me your number: ")
while switch:
    if number[0] == 8 or 9:
        if number[1] == number[2]:
            if number[3] == 8 or 9:
                print("Call is from a telemarketer")
                switch = False
            else:
                print("Call is fortunately not from a telemarketer")
                break
        else:
            print("Call is fortunately not from a telemarketer")
            break
    else:
        print("Call is fortunately not from a telemarketer")
        break



