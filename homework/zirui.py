from collections import defaultdict

count = 1
count_list = []

tiles_dict = defaultdict(int)

for i in range(10):
    tiles_dict[i] = 1000
while True:
    count_list = list(str(count))

    # if len(count_list) < 4:
    #     for j in range(4 - (len(count_list))):
    #         count_list.append("0")

    count_list += ['0'] * (4 - len(count_list))


    for k in range(len(count_list)):
        tiles_dict[int(count_list[k])] -= 1
    for l in range(len(tiles_dict)):
        if tiles_dict[l] == 0:
            print(count)
            exit()
    count += 1