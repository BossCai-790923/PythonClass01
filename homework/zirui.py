printed_list = [["_", "_", "_", "_", "_", "_", "_", "_", "_"], ["0 0", "0 1", "0 2", "1 0", "1 1", "1 2", "2 0", "2 1", "2 2"]]
turn = 1


def player_turn(player):
    print(f"Player {player}'s turn!")
    return input("New coordinates: ")


def coord_change(players_turn, coords):
    if players_turn == 1:
        printed_list[0][printed_list[1].index(coords)] = "O"
    if players_turn == 2:
        printed_list[0][printed_list[1].index(coords)] = "X"


def print_board():
    for i in range(len(printed_list[0])):
        print(printed_list[0][i], end=" ")
        if (i + 1) % 3 == 0:
            print(end="\n")


def prevent_overlap(coordi):
    if printed_list[0][printed_list[1].index(coordi)] == "O" or printed_list[0][printed_list[1].index(coordi)] == "X":
        print("These coordinates are invalid.")
        return 1
    else:
        return 0


def check_win(player):
    if player == 1:
        game_unit = "O"
    else:
        game_unit = "X"
    if printed_list[0][0] == printed_list[0][1] == printed_list[0][2] == game_unit:
        print(f"Player {player} win!")
        exit()
    if printed_list[0][3] == printed_list[0][4] == printed_list[0][5] == game_unit:
        print(f"Player {player} win!")
        exit()
    if printed_list[0][6] == printed_list[0][7] == printed_list[0][8] == game_unit:
        print(f"Player {player} win!")
        exit()
    if printed_list[0][0] == printed_list[0][3] == printed_list[0][6] == game_unit:
        print(f"Player {player} win!")
        exit()
    if printed_list[0][1] == printed_list[0][4] == printed_list[0][7] == game_unit:
        print(f"Player {player} win!")
        exit()
    if printed_list[0][3] == printed_list[0][5] == printed_list[0][8] == game_unit:
        print(f"Player {player} win!")
        exit()
    if printed_list[0][1] == printed_list[0][4] == printed_list[0][8] == game_unit:
        print(f"Player {player} win!")
        exit()
    if printed_list[0][7] == printed_list[0][4] == printed_list[0][6] == game_unit:
        print(f"Player {player} win!")
        exit()


print("Tic Tac Toe game starts!")
print("------------------------")
while True:
    coord = player_turn(turn)
    if prevent_overlap(coord) == 1:
        continue
    if prevent_overlap(coord) == 0:
        coord_change(turn, coord)
        print_board()
        check_win(turn)
        if turn == 1:
            turn = 2
            continue
        if turn == 2:
            turn = 1