file_path = '/Users/korbinianschleifer/Desktop/input.txt'

instructions = []

with open(file_path, 'r') as file:
    for line in file:
        line = line[:-1]
        arr = line.split()
        instructions.append({"instruction": arr[0], "amount": int(arr[1])})

### Part 1 ###
x_value, y_value = 0, 0

for dict in instructions:
    X = dict["amount"]
    if dict["instruction"] == "forward":
        x_value += X
    elif dict["instruction"] == "down":
        y_value += X
    else:
        y_value -= X

print("solution 1: ", x_value * y_value)

### Part 2 ###
aim, horizontal, depth = 0, 0, 0

for dict in instructions:
    X = dict["amount"]
    if dict["instruction"] == "down":
        aim += X
    elif dict["instruction"] == "up":
        aim -= X
    else:
        horizontal += X
        depth += aim * X

print("solution 2: ", horizontal * depth)
