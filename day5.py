file_path = '/Users/korbinianschleifer/desktop/advent-of-code-2021/inputs/day5.txt'

lines = []

with open(file_path, 'r') as file:
    for line in file:
        line = line[:-1].split()
        line.remove('->')
        start_of_line = line[0].split(',')
        end_of_line = line[1].split(',')
        points = {
            'x1': int(start_of_line[0]),
            'y1': int(start_of_line[1]),
            'x2': int(end_of_line[0]),
            'y2': int(end_of_line[1])
        }
        lines.append(points)


### Part 1 ###

# filter the lines to get all straight lines
def get_all_straight_lines(lines):
    straight_lines = []
    for line in lines:
        if line['x1'] == line['x2'] or line['y1'] == line['y2']:
            straight_lines.append(line)
    return straight_lines

# get all points from start to end of straight lines
def get_all_points_for_straight_lines(lines):
    points = []
    for line in lines:
        if line['x1'] == line['x2']:
            similar, start, end = line['x1'], line['y1'], line['y2']

            # iterate through difference and add all points
            start, end = min(start, end), max(start, end)
            for i in range(start, end + 1):
                point = {
                    'x': similar,
                    'y': i
                }
                points.append(point)

        elif line['y1'] == line['y2']:
            similar, start, end = line['y1'], line['x1'], line['x2']

            # iterate through difference and add all points
            start, end = min(start, end), max(start, end)
            for i in range(start, end + 1):
                point = {
                    'x': i,
                    'y': similar
                }
                points.append(point)

    return points

def find_max_x_y(lines):
    max_x = 0
    max_y = 0
    for line in lines:
        if line['x1'] > max_x or line['x2'] > max_x:
            max_x = max(line['x1'], line['x2'])
        if line['y1'] > max_y or line['y2'] > max_y:
            max_y = max(line['y1'], line['y2'])
    return max_x, max_y

# create a board -> 2d array
def create_board(x, y):
    # create board with all dots as strings and return
    x += 1
    y += 1
    board = []
    for i in range(x):
        board.append(['.'] * y)
    return board
        
# mark all points on the board
def mark_points_on_board(points, board):
    for point in points:
        x, y = point['x'], point['y']
        if board[x][y] == '.':
            board[x][y] = 1
        else:
            board[x][y] += 1

# iterate over the board to count points > 1
def count_board_for_overlap(board):
    crossings = 0
    for line in board:
        for point in line:
            if type(point) != str and point > 1:
                crossings += 1
    return crossings

straight_lines = get_all_straight_lines(lines)
points = get_all_points_for_straight_lines(straight_lines)
max_x, max_y = find_max_x_y(straight_lines)
board = create_board(max_x, max_y)
mark_points_on_board(points, board)
solution1 = count_board_for_overlap(board)

print(solution1)


### Part 2 ###

# easy cases:
# case 1: x1 < x2 and y1 < y2 (5,10)(10,15)
    # -> increment x1, y1 until x2, y2 reached
# case 2: x1 > x2 and y1 > y2 (10,15)(5,10)
    # -> increment x2, y2 until x1, y1 reached

# harder cases:
# case 1: x1 < x2 and y1 > y2 (5,10)(10,5)
    # -> increment x1, decrement y1 until x2, y2 reached
# case 2: x1 > x2 and y1 < y2 (10,5)(5,10)
    # -> decrement x1, increment y1

def get_all_diagonal_lines(lines):
    diagonal_lines = []
    for line in lines:
        if line['x1'] != line['x2'] or line['y1'] != line['y2']:
            diagonal_lines.append(line)
    return diagonal_lines

def add_easy_points(points, x1, y1, x2, y2):
    # x1 and y1 are always the smaller coordinates
    x1, y1, x2, y2 = min(x1, x2), min(y1, y2), max(x1, x2), max(y1, y2)
    # increment until bigger point is reached
    while x1 <= x2 and y1 <= y2:
        point = {
            'x': x1,
            'y': y1
        }
        points.append(point)
        x1 += 1
        y1 += 1
    return points

def add_uneven_points_case_1(points, x1, y1, x2, y2):
    # increment x1 and decrement y1
    while x1 <= x2 and y1 >= y2:
        point = {
            'x': x1,
            'y': y1
        }
        points.append(point)
        x1 += 1
        y1 -= 1
    return points

def add_uneven_points_case_2(points, x1, y1, x2, y2):
    # increment y1 and decrement x1
    while x1 >= x2 and y1 <= y2:
        point = {
            'x': x1,
            'y': y1
        }
        points.append(point)
        x1 -= 1
        y1 += 1
    return points

# get all points from start to end of diagonal lines
def get_all_points_for_diagonal_lines(points, lines):
    for line in lines:
        x1, y1, x2, y2 = line['x1'], line['y1'], line['x2'], line['y2']

        # easy case: either first point is smaller or second point is smaller
        if (x1 < x2 and y1 < y2) or (x1 > x2 and y1 > y2):
            points = add_easy_points(points, x1, y1, x2, y2)       

        # uneven points case 1
        elif (x1 < x2 and y1 > y2):
            points = add_uneven_points_case_1(points, x1, y1, x2, y2)

        # uneven points case 2
        elif (x1 > x2 and y1 < y2):
            points = add_uneven_points_case_2(points, x1, y1, x2, y2)

    return points

straight_lines = get_all_straight_lines(lines)
diagonal_lines = get_all_diagonal_lines(lines)
points = get_all_points_for_straight_lines(straight_lines)
points = get_all_points_for_diagonal_lines(points, diagonal_lines)
max_x, max_y = find_max_x_y(lines)
board = create_board(max_x, max_y)
mark_points_on_board(points, board)
solution2 = count_board_for_overlap(board)

print(solution2)
