import copy
file_path = '/Users/korbinianschleifer/desktop/advent-of-code-2021/inputs/day4.txt'

random_nums, bingo_boards = [], []

with open(file_path, 'r') as file:
    current_board = []
    for i, line in enumerate(file):
        line = line[:-1]
        if i == 0:
            # first line are the random numbers
            random_nums = line.split(',')
            random_nums = list(map(int, random_nums))
            continue
        if len(line) == 0:
            # new board starts with next line
            bingo_boards.append(current_board)
            current_board = []
            continue
        line = line.split()
        current_board.append(list(map(int, line)))

# remove empty first board
bingo_boards.pop(0)
            
### Part 1 ###
# sets a number to -1 if drawn
def mark_as_complete(boards, num):
    for board in boards:
        for line in board:
            for i, x in enumerate(line):
                if x == num: line[i] = -1

# check if a row is bingo
def row_is_bingo(board):
    for line in board:
        if all(x == -1 for x in line):
            return True
    return False

# check if a column is bingo
def column_is_bingo(board):
    for i in range(len(board)):
        col = [line[i] for line in board]
        if all(x == -1 for x in col):
                return True
    return False

# check all bingo boards for bingo
def is_bingo(boards):
    for board in boards:
        if row_is_bingo(board) or column_is_bingo(board):
            return board
    return False

# calculate the sum of unchecked nums of a bingo board
def sum_of(board):
    board_sum = 0
    for line in board:
        for num in line:
            if num != -1: board_sum += num
    return board_sum

# draw a number and mark it as complete on all boards
solution1 = 0
for num in random_nums:
    mark_as_complete(bingo_boards, num)
    solution_board = is_bingo(bingo_boards)
    if solution_board:
        solution1 = sum_of(solution_board) * num
        break

print(solution1)


### Part 2 ###
for i, num in enumerate(random_nums):
    mark_as_complete(bingo_boards, num)
    while is_bingo(bingo_boards) and len(bingo_boards) > 1:
        solution_board = is_bingo(bingo_boards)
        bingo_boards.remove(solution_board)
    if len(bingo_boards) == 1 and is_bingo(bingo_boards):
        solution2 = sum_of(bingo_boards[0]) * num
        break

print(solution2)