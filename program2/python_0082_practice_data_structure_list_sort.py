my_list = []
new_number_str = input("Next number:")

while 'exit' != new_number_str:
    new_number = int(new_number_str)
    my_list.append(new_number)
    new_number_str = input("Next number:")

my_list.sort()
print(my_list)


