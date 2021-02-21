# merge
list_a = [1, 5, 7, 9, 13, 15, 24, 27, 78, 110, 167]
list_b = [2, 2, 6, 8, 16, 17, 18, 19, 99]
# to list_ab
# merge
list_c = [1, 5, 7]
list_d = [2, 2, 6, 8, 16, 17, 18, 19, 99]
# to list_cd
# merge
list_e = []
list_f = [2, 2, 6, 8, 16, 17, 18, 19, 99]
# to list_ef

new_list = []
index_a = 0
index_b = 0
for n in range(len(list_a) + len(list_b)):
    if index_a == len(list_a):
        new_list.extend(list_b[list_b:])
    if index_b == len(list_b):
        new_list.extend(list_a[index_a:])
    if list_a[index_a] >= list_b[index_b]:
        new_list.append(list_b[index_b])
        index_b += 1
        new_list.append(list_a[index_a])
        index_a += 1
    else:
        new_list.append(list_a[index_a])
        index_a += 1
        new_list.append(list_b[index_b])
        index_b += 1
print(new_list)
