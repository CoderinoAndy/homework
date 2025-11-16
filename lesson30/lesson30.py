# Lesson 30
rows = 10
for rownum in range(rows):
    current_output = ""
    i = 0
    while i <= rownum:
        if i%2 == 0 or i == 0:
            current_output += "1"
            i += 1
        else:
            current_output += "0"
            i += 1
    print(current_output)
