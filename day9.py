file_path = './inputs/day9.txt'

field = []

with open(file_path, 'r') as file:
    for line in file:
        line = line[:-1]
        nums = [int(num) for num in line]
        nums.insert(0,9)
        nums.append(9)
        field.append(nums)

# add 9 outside of the field to make calculation easier
line_of_nines = [9] * len(field[0])
field.insert(0, line_of_nines)
field.append(line_of_nines)

### Part 1 ###
def is_local_minimum(field, y, x):
    val = field[y][x]
    up, down = field[y-1][x], field[y+1][x]
    right, left = field[y][x+1], field[y][x-1]

    if val < min(up, right, down, left):
        return True
    return False
    
def find_low_points(minimums, field):
    for y in range(1, len(field) - 1):
        for x in range(1, len(field[y]) - 1):
            if is_local_minimum(field, y, x):
                minimums[(y, x)] = field[y][x]

minimums = {}
find_low_points(minimums, field)
solution1 = sum(minimums.values()) + len(minimums)

print(solution1)

### Part 2 ###
# depth first search
visited = set()

def get_all_adjacent_points(y, x):
    return [(y-1,x), (y,x+1), (y+1,x), (y,x-1)]

def get_basin_size(y, x):
    if field[y][x] == 9:
        return 0
    # check that point was not already visited
    if (y, x) in visited:
        return 0
    # add point to visited
    visited.add((y, x))
    size = 1
    points = get_all_adjacent_points(y, x)
    for point in points:
        if point not in visited:
            size += get_basin_size(point[0], point[1])

    return size


def calculate_basin_sizes(minimums):
    basin_sizes = []
    for keys in minimums:
        y, x = keys[0], keys[1]
        count = get_basin_size(y, x) 
        basin_sizes.append(count)
    return basin_sizes

basin_sizes = calculate_basin_sizes(minimums)
max_vals = sorted(basin_sizes, reverse=True)[:3]
print(max_vals[0] * max_vals[1] * max_vals[2])