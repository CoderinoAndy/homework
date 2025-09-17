# Lesson 4
def fenceplank():
    fencePlank_number = 0
    for _ in range(3):
        fences_input = input()
        fencePlank_number += len(fences_input)

    paintLeftOver = 12 - fencePlank_number % 12

    dozensrequired = round(fencePlank_number/12)
    if dozensrequired == 0 and fencePlank_number != 0:
        dozensrequired = 1


    print(fencePlank_number)
    print(paintLeftOver)
    print(dozensrequired*14.95)
fenceplank()