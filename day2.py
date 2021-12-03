file_path = '/Users/korbinianschleifer/Desktop/input.txt'

instructions = []

with open(file_path, 'r') as file:
    for line in file:
        line = line[:-1]
        arr = line.split()
        instructions.append({"instruction": arr[0], "amount": int(arr[1])})

x_value = 0;
y_value = 0;

for dict in instructions:
    if dict["instruction"] == "forward":
        x_value += dict["amount"]
    elif dict["instruction"] == "down":
        y_value += dict["amount"]
    else:
        y_value -= dict["amount"]

print(x_value * y_value)
