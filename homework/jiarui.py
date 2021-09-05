borko_moves = str(input("Please input a string of at most 50 characters to indicate Borko's moves: "))
if len(borko_moves) > 50:
    print("Invalid Input")

ball_location = [1, 0, 0]
for char in borko_moves:
    cupA = ball_location[0]
    cupB = ball_location[1]
    cupC = ball_location[2]
    if char == 'A':
        ball_location[0] = cupB
        ball_location[1] = cupA
        ball_location[2] = cupC
    if char == 'B':
        ball_location[0] = cupA
        ball_location[1] = cupC
        ball_location[2] = cupB
    if char == 'C':
        ball_location[0] = cupC
        ball_location[1] = cupB
        ball_location[2] = cupA

for i in range(len(ball_location)):
    if ball_location[i] == 1:
        print(i+1)
