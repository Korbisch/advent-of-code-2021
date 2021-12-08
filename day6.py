import copy
file_path = '/Users/korbinianschleifer/desktop/advent-of-code-2021/inputs/day6.txt'

input_row = []

with open(file_path, 'r') as file:
    for line in file:
        line = line[:-1]
        input_row = line.split(',')
        input_row = [int(val) for val in input_row]

### Part 1 ###
current_nums = dict()
for i in range(9):
    current_nums[i] = input_row.count(i)

def decrement_days_get_zeros(nums):
    zero_count = nums[0]
    for i in range(8):
        nums[i] = nums[i + 1]
    nums[6] += zero_count
    nums[8] = 0
    return nums, zero_count

def create_new_fish(zero_count, current_nums):
    current_nums[8] = zero_count
    return current_nums

# iteration
for _ in range(80):
    current_nums, zero_count = decrement_days_get_zeros(current_nums)
    current_nums = create_new_fish(zero_count, current_nums)

solution1 = 0
for i in range(9):
    solution1 += current_nums[i]

print(solution1)

### Part 2 ###
for _ in range(256-80):
    current_nums, zero_count = decrement_days_get_zeros(current_nums)
    current_nums = create_new_fish(zero_count, current_nums)

solution2 = 0
for i in range(9):
    solution2 += current_nums[i]

print(solution2)