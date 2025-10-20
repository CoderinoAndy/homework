from math import ceil
plank1 = len(input("Plank 1: "))
plank2 = len(input("Plank 2: "))
plank3 = len(input("plank 3: "))
planksrequired = plank1 + plank2 + plank3
dozensrequired = ceil(planksrequired/12)
cost = dozensrequired*14.95

print(f"Total planks required: {planksrequired}")
print(f"Total packages required: {dozensrequired}")
print(f"Total cost: {cost}")
