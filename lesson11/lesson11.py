# Lesson 11
coordinate = input()
coordinate_list = coordinate.split(",")
listMapped = list(map(int, coordinate_list))
x = listMapped[0]
y = listMapped[1]

if x > 0 and y > 0:
    print(f"Quadrant 1: {x, y}")
elif x > 0 and y < 0:
    print(f"Quadrant 4: {x, y}")
elif x < 0 and y > 0:
    print(f"Quadrant 2: {x, y}")
elif x < 0 and y < 0:
    print(f"Quadrant 3: {x, y}")
elif x == 0 and y == 0:
    print(f"You are at the center: {x, y}")
elif x == 0:
    print(f"You are on the Y-axis: {x, y}")
else:
    print(f"You are on the X-axis: {x, y}")
