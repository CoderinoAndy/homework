# Lesson 12
triangle = []
while True:
    counter = 1
    for _ in range(3):
        angle = int(input(f"angle {counter}: "))
        triangle.append(angle)
        counter += 1

    if sum(triangle) != 180:
        print("3 angles of a triangle must equal to 180 degrees.")
        triangle.clear()
        continue
    else:
        break

if triangle[0] == triangle[1] == triangle[2]:
    print("Equilateral Triangle")
elif triangle[0] == triangle[1] or triangle[1] == triangle[2] or triangle[2] == triangle[0]:
    print("Isosceles Triangle")
else:
    print("Scalene Triangle")