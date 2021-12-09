import statistics
file_path = './inputs/day7.txt'

input_row = []

with open(file_path, 'r') as file:
    for line in file:
        line = line[:-1]
        input_row = line.split(',')
        input_row = [int(val) for val in input_row]

### Part 1 ###
median = int(statistics.median(input_row))

distance = 0
for el in input_row:
    distance += abs(el - median)

print(distance)

### Part 2 ###
mean = int(statistics.mean(input_row))

distance2 = 0
# using the Gauss formula
for el in input_row:
    n = abs(el - mean)    
    distance2 += (n*(n+1))/2

print(int(distance2))