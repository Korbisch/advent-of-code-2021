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
def mark_lines_on_board(points, board):
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
mark_lines_on_board(points, board)
solution1 = count_board_for_overlap(board)

print(solution1)

