import copy
file_path = '/Users/korbinianschleifer/desktop/advent-of-code-2021/inputs/day3.txt'

binary_nums = []

with open(file_path, 'r') as file:
    for line in file:
        line = line[:-1]
        binary_nums.append(line)

### Part 1 ###
columns = len(binary_nums[0])
count = [0] * columns
for line in binary_nums:
    for i, val in enumerate(line):
        if val == "1":
            count[i] += 1

total = len(binary_nums)
gamma_rate = [0] * columns
epsilon_rate = [1] * columns
for i, val in enumerate(count):
    if val > total // 2:
        gamma_rate[i] = 1
        epsilon_rate[i] = 0

gamma_rate.insert(0, "0b")
epsilon_rate.insert(0, "0b")

gamma_rate = ''.join(str(e) for e in gamma_rate)
epsilon_rate = ''.join(str(e) for e in epsilon_rate)

solution1 = int(gamma_rate, 2) * int(epsilon_rate, 2)
print(solution1)

### Part 2 ###
def get_most_common_bit(arr, col):
    zeros = 0
    ones = 0
    for line in arr:
        if line[col] == "1":
            ones += 1
        else:
            zeros += 1
    return "1" if ones >= zeros else "0"

def get_least_common_bit(arr, col):
    zeros = 0
    ones = 0
    for line in arr:
        if line[col] == "1":
            ones += 1
        else:
            zeros += 1
    return "0" if zeros <= ones else "1"

# oxygen rating
oxygen_rating = copy.deepcopy(binary_nums)
for index in range(columns):
    most_common_bit = get_most_common_bit(oxygen_rating, index)
    oxygen_rating = [x for x in oxygen_rating if x[index] == most_common_bit]
    if len(oxygen_rating) == 1:
        break

# co2 rating
co2_rating = copy.deepcopy(binary_nums)
for index in range(columns):
    least_common_bit = get_least_common_bit(co2_rating, index)
    co2_rating = [x for x in co2_rating if x[index] == least_common_bit]
    if len(co2_rating) == 1:
        break

solution2 = int('0b' + oxygen_rating[0], 2) * int('0b' + co2_rating[0], 2)
print(solution2)