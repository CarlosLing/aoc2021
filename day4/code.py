import numpy as np 

with open('day4/input.txt') as f: 
    lines = f.readlines()

# Reading 
bingo_numbers = lines[0][:-1].split(',')
bingo_numbers = np.array(bingo_numbers).astype(int)

boards = []
new_board = None
for line in lines[1:]:
    if line =='\n':
        if new_board is not None:
            boards.append(new_board)
        new_board = []

    else: 
        line_clean = line[:-1].split(' ')
        line_clean = [int(i) for i in line_clean if i != '']
        new_board.append(line_clean)

boards = np.array(boards)

def check_boards(boards_checks, n_rows = 5):
    is_bingo = False
    num_board = None

    s_cols = np.sum(boards_checks, axis=2) 
    s_rows = np.sum(boards_checks, axis=1)
    if np.max(s_cols) >= n_rows:
        is_bingo = True
        num_board = int(np.argmax(s_cols) / n_rows)
    if np.max(s_rows) >= n_rows:
        is_bingo = True
        num_board = int(np.argmax(s_rows) / n_rows)

    return is_bingo, num_board

l = len(boards)

for i in range(l):

    boards_checks = boards == bingo_numbers[0]

    for cantado in bingo_numbers[1:]: 
        check_cantado = boards == cantado
        boards_checks = check_cantado + boards_checks
        
        is_bingo, board_index = check_boards(boards_checks)
        if is_bingo: 
            break

    results = np.sum(boards[board_index] * (1 - boards_checks[board_index]))*cantado
    loosing_board = boards[board_index]
    boards = np.delete(boards, board_index, 0)

