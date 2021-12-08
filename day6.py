file_path = './inputs/day6.txt'

input_row = []

with open(file_path, 'r') as file:
    for line in file:
        line = line[:-1]
        input_row = line.split(',')
        input_row = [int(val) for val in input_row]

### Part 1 ###
# saving all the fish in a dictionary {0: count, 1: count, ...}
current_nums = dict()
for i in range(9):
    current_nums[i] = input_row.count(i)

def decrement_days_get_zeros(nums):
    zero_count = nums[0]
    for i in range(8):
        nums[i] = nums[i + 1]
    nums[6] += zero_count
    nums[8] = 0
    return zero_count

# iteration
for _ in range(80):
    zero_count = decrement_days_get_zeros(current_nums)
    current_nums[8] = zero_count

solution1 = 0
for i in range(9):
    solution1 += current_nums[i]

print(solution1)

### Part 2 ###
for _ in range(256-80):
    zero_count = decrement_days_get_zeros(current_nums)
    current_nums[8] = zero_count

solution2 = 0
for i in range(9):
    solution2 += current_nums[i]

print(solution2)