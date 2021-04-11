num_list = [1, 2, 4, 3, 7, 4, 2, 5, 6]

moves = 0
num_len = len(num_list)
num_list.sort()

largest_num = num_list[num_len - 1]
if largest_num > num_len:
    print("This list is invalid.")
    exit()

for i in range(len(num_list)):
    largest_num = num_list[num_len - i - 1]
    moves += abs(largest_num - len(num_list))
    num_list.remove(largest_num)
if moves > 200000:
    print(-1)
else:
    print(moves)