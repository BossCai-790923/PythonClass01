list_a = [1,5,7,9,13,15,24,27,78,110,167]
# list_a = [1,5,7]
# list_a = [1, 5]
# list_b = [2, 7]
# list_a = []
# list_b = [2,2,6,8,16,17,18,19,99]
#
# list_a = []
list_b = []

new_list = []
index_a = 0
index_b = 0

while True:

    # Situation 1)
    if index_a == len(list_a):
        new_list.extend(list_b[index_b:])
        break

    # Situation 2)
    if index_b == len(list_b):
        new_list.extend(list_a[index_a:])
        break

    # Situation 3)
    if list_a[index_a] < list_b[index_b]:
        new_list.append(list_a[index_a])
        index_a += 1
    else:
        new_list.append((list_b[index_b]))
        index_b += 1

print(new_list)












