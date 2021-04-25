chess_board = [['_','_','_'],['_','_','_'],['_','_','_']]


def print_chessboard(chess_bard):
    for row in chess_bard:
        print(*row)


def get_user_coordinates():
    input_value = input("New coordinates: ")
    x_y_list = input_value.split(' ') # if user input '1 2', x_y_list will become list ['1', '2']
    x = int(x_y_list[0])
    y = int(x_y_list[1])
    return [x, y]


def check_coordinates(chess_board, coordinates):
    x = coordinates[0]
    y = coordinates[1]

    if x < 0 or x > 2:  # invalid x
        print(f"Coordinates x is wrong {x}. Valid value is in range[0, 2]. Please try again.")
        return False

    if y < 0 or y > 2:  # invalid y
        print(f"Coordinates y is wrong {y}. Valid value is in range[0, 2]. Please try again.")
        return False

    if chess_board[x][y] != '_':
        print(f"chessboard [{x}][{y}] has value {chess_board[x][y]}. Pleass try again.")
        return False

    return True


def check_win(chess_board, coordinates):
    x = coordinates[0]
    y = coordinates[1]

    if chess_board[x][0] == chess_board[x][1] and chess_board[x][0] == chess_board[x][2]:
        print("Win!")
        exit()

    if chess_board[0][y] == chess_board[1][y] and chess_board[0][y] == chess_board[2][y]:
        print("Win!")
        exit()

    if x == 0 and y == 0 or x == 2 and y == 2 or x == 1 and y == 1:
        if chess_board[0][0] == chess_board[1][1] and chess_board[0][0] == chess_board[2][2]:
            print("Win!")
            exit()

    if x == 0 and y == 2 or x == 2 and y == 0 or x == 1 and y == 1:
        if chess_board[2][0] == chess_board[1][1] and chess_board[2][0] == chess_board[0][2]:
            print("Win!")
            exit()


def place_piece(chess_board, piece):
    while True:
        coordinates = get_user_coordinates()
        is_valid_coordinates = check_coordinates(chess_board,coordinates)
        if is_valid_coordinates:
            break

    chess_board[coordinates[0]][coordinates[1]] = piece
    print_chessboard(chess_board)
    check_win(chess_board, coordinates)
    print('_' * 20)


#--CODE ADD BEGIN -------------------------------------------------------------

'''
===============
Thinking Logic 
===============
----------------------------------------------
For all python program, step 1) prepare 'data'
Everything is about data. They key is how to organize the data.
----------------------------------------------

There are in total 8 lines in chess_board.
Each line is composed of 3 dots.
Each dot is a cooridnates which has 2 values - x and y.

# 3 horizontal lines
[[0,0],[0,1],[0,2]]
[[1,0],[1,1],[1,2]]
[[2,0],[2,1],[2,2]]

# 3 vertical lines
[[0,0],[1,0],[2,0]]
[[0,1],[1,1],[2,1]]
[[0,2],[1,2],[2,2]]

2 skew lines
[[0,0],[1,1],[2,2]]
[[0,2],[1,1],[2,0]]

lines = [
[[0,0],[0,1],[0,2]], [[1,0],[1,1],[1,2]], [[2,0],[2,1],[2,2]],              # 3 horizontal lines
[[0,0],[1,0],[2,0]], [[0,1],[1,1],[2,1]], [[0,2],[1,2],[2,2]],              # 3 vertical lines
[[0,0],[1,1],[2,2]], [[0,2],[1,1],[2,0]]                                    # 2 skew lines
]

These 8 lines can be grouped into 6 categories: 
Category 1) Almost win lines: There are 2 'X' and 1 '_'
Category 2) Potential win lines: There are 1 'X' and 2 '_'
Category 3) Almost lose lines: There are 2 'O' and 1 '_'
Category 4) Potential lose lines: There are 1 'O' and 2 '_'
Category 5) Useless lines: There are 'O' and 'X'
Category 6) Empty lines: There are 3 '_'

Initially, all 8 lines are in category 6) Empty lines.
So, let's define these groups.

almost_win_lines = []           # 2 'X' and 1 '_'
potential_win_lines = []        # 1 'X' and 2 '_'
almost_lose_lines = []          # 2 'O' and 1 '_'
potential_lose_lines = []       # 1 'O' and 2 '_'
uselss_lines = []               # contains both 'X' and 'O'
empty_lines = list(lines)       # contains 3 '_'


Each time when a 'X' or a 'O' is placed in chess_board, at least 2 lines will be updated, we need to update those lines, move them to the correct groups.

so 2 extra functions should be defined:

def update_lines_after_ai_player(coordinates):
    pass 
def update_lines_after_human_player(coordinates):
    pass 


'''


lines = [
[[0,0],[0,1],[0,2]], [[1,0],[1,1],[1,2]], [[2,0],[2,1],[2,2]],              # 3 horizontal lines
[[0,0],[1,0],[2,0]], [[0,1],[1,1],[2,1]], [[0,2],[1,2],[2,2]],              # 3 vertical lines
[[0,0],[1,1],[2,2]], [[0,2],[1,1],[2,0]]                                    # 2 skew lines
]

almost_win_lines = []           # 2 'X' and 1 '_'
potential_win_lines = []        # 1 'X' and 2 '_'
almost_lose_lines = []          # 2 'O' and 1 '_'
potential_lose_lines = []       # 1 'O' and 2 '_'
useless_lines = []               # contains both 'X' and 'O'
empty_lines = list(lines)       # contains 3 '_'


def update_lines_after_ai_player(coordinates):

    for line in almost_win_lines:
        if coordinates in line:
            print("Win!")
            exit()

    for line in almost_lose_lines[:]:
        if coordinates in line:
            almost_lose_lines.remove(line)
            useless_lines.append(line)

    for line in potential_win_lines[:]:
        if coordinates in line:
            potential_win_lines.remove(line)
            almost_win_lines.append(line)

    for line in potential_lose_lines[:]:
        if coordinates in line:
            potential_lose_lines.remove(line)
            useless_lines.append(line)

    for line in empty_lines[:]:
        if coordinates in line:
            empty_lines.remove(line)
            potential_win_lines.append(line)


def update_lines_after_human_player(coordinates):
    pass








def place_piece_by_computer(chess_board, piece):
    computer_coordinates = get_computer_coordinates(chess_board)
    chess_board[computer_coordinates[0]][computer_coordinates[1]] = piece
    print_chessboard(chess_board)
    check_win(chess_board, computer_coordinates)
    print('_' * 20)

#--CODE ADD END -------------------------------------------------------------






welcome_msg = '''Tic Tac Toe Game Starts:
--------------------------------------------
'''

print(welcome_msg)

print_chessboard(chess_board)

player1 = ['PLAYER 1', 'O']
player2 = ['PLAYER 2', 'X']
players = [player1, player2]

for turn in range(9):
    player = players[turn % 2]
    print(f"{player[0]}'s turn:")

    # CODE DELETE BEGIN -------------------
    # place_piece(chess_board, player[1])
    # CODE DELETE END -------------------

    # --CODE ADD BEGIN -------------------
    if 'PLAYER 1' == player[0]:
        place_piece(chess_board, player[1])
    else:
        place_piece_by_computer(chess_board, player[1])
    # --CODE ADD END -------------------

print("Draw!")