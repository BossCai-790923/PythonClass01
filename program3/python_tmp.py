line = ['_'] * 19
chess_board = [line] * 19

def print_chessboard(chess_bard):
    for row in chess_bard:
        print(*row)

print_chessboard(chess_board)