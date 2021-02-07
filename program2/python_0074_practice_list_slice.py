number_list = list(range(100))
print(number_list)

# Requirement 1 Use slice generate list 10,11,12 ... 20
# -> start = 10; stop = 21(exclusive), step = 1
list1 = number_list[10:21]
print(list1)


# Requirement 2 Use slice generate list 1,3,5,7,9 ... 99
# -> start = 1; stop = 100 which is the last one, I can omit the stop parameter; step = 2
list1 = number_list[1::2]
print(list1)


# Requirement 3 Use slice generate list 9,11,13,15 ... 49
# -> start = 9; stop = 50(exclusive); step = 2
list1 = number_list[9:50:2]
print(list1)


# Requirement 4 Use slice generate list 98,96,94,92 ... 0
# -> start = 98; stop = 0, which is the first one, so I can omit it; step = -2
list1 = number_list[98::-2]
print(list1)


# Requirement 5 Use slice generate list 50,48,46,44 ... 10
# -> start = 50; stop = 9; step = -2
list1 = number_list[50:9:-2]
print(list1)

