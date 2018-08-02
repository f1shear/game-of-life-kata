
DEAD = '.'
ALIVE = '*'


def get_cell_state(x, y, board):
    length = len(board)
    width = len(board[0])
    if x >= 0 and y >= 0 and x < length and y < width:
        if board[x][y] == ALIVE:
            return 1
    return 0


def calculate_next_life(x, y, board):
    current_state = board[x][y]
    new_state = current_state
    length = len(board)
    width = len(board[0])

    neighbours = [
        (x, y-1), (x, y+1),  # left, right
        (x-1, y), (x+1, y),  # top, bottom
        (x-1, y-1), (x-1, y+1),  # top left, top right
        (x+1, y-1), (x+1, y+1),  # bottom left, bottom right
    ]

    # Count alive neighbours for the cell
    count = 0
    for pos in neighbours:
        count += get_cell_state(pos[0], pos[1], board)

    # Apply rules and get new state
    if current_state == ALIVE:
        if count < 2:
            new_state = DEAD
        elif count > 3:
            new_state = DEAD
        elif count == 2 or count == 3:
            pass
    else:
        if count == 3:
            new_state = ALIVE
    return new_state


def generate_board(board):
    length = len(board)
    width = len(board[0])
    output = []
    for i in range(length):
        output.append([None] * width)
    return output


def validate_board(board):
    if len(board) == 0:
        raise Exception("Invalid board")


def process_board(board):
    validate_board(board)
    output = generate_board(board)
    for i in range(len(board)):
        for j in range(len(board[0])):
            output[i][j] = calculate_next_life(i, j, board)
    return output


def main(board):
    output = process_board(board)


def test_process_board():
    board = [
        ['.', '.', '*', '.'],
        ['.', '*', '*', '*'],
        ['*', '.', '*', '.'],
    ]
    output = process_board(board)
    expected_board = [
        ['.', '*', '*', '*'],
        ['.', '.', '.', '*'],
        ['.', '.', '*', '*'],
    ]
    # check if output and expected board is same
    for i in range(len(output)):
        for j in range(len(output[i])):
            assert output[i][j] == expected_board[i][j]


if __name__ == '__main__':
    test_process_board()
