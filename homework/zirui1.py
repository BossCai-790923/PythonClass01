list_a = [1,2]
list_b = [3,4]

new_list = []
index_a = 0
index_b = 0

while True:

    index_a = index_a + 1
    index_b = index_b + 1

    if index_a == len(list_a) - 1:
        new_list = new_list + list_b
        break

    elif index_b == len(list_b) - 1:
        new_list = new_list + list_a
        break

    elif index_a == len(list_a) - 1 and index_b == len(list_b) - 1:
        if list_a[0] > list_b[0]:
            new_list.append(list_b[0])
        else:
            new_list.append(list_a[0])
        break

    elif index_a != len(list_a) - 1 and index_b != len(list_b) - 1:
        if len(list_a) == 0:
            new_list = new_list + list_b
            break

        elif len(list_b) == 0:
            new_list = new_list + list_a
            break

        if list_a[0] < list_b[0]:
            new_list.append(list_a.pop(0))
            list_b.pop(0)

        elif list_a[0] > list_b[0]:
            new_list.append(list_b.pop(0))
            list_a.pop(0)

print(new_list)