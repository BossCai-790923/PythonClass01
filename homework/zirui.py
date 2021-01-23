num_list = [int(input("Enter a number: "))]

while True:
    num = int(input("Enter a number: "))
    num_list.append(num)
    while True:
        num_index = num_list.index(num)
        if num < num_list[num_index-1]:
            print(num)
            num_list.remove(num)
            num_list.insert(num_index-1, num)
        else:
            print("b")
            break
        num_index = num_list.index(num)
        if num_index == 0:
            break
        if num > num_list[num_index-1]:
            break
    print(num_list)