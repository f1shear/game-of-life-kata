

def calculate_next_life(x, y, board):
    # True for alive
    # False for dead
    return state


def process_board(board):
    output = board
    return output


def main(board):
    output = process_board(board)
    print(output)


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
