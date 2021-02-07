'''
Requirement: cut and swap
Requirement 1) create a list which contains 10 int numbers from 1 to 10
Requirement 2) let user to input a 'cut' number: from 1 to 9
Requirement 3) You cut the list in 2 parts at index 'cut', and you swap the 2 parts, print the new list
'''


# Requirement 1) create a list which contains 10 int numbers from 1 to 10
original_list = list(range(1,11))
print(original_list)



# Requirement 2) let user to input a 'cut' number: from 1 to 9
cut = int(input("Cut number (1 - 9): "))


# Requirement 3) You cut the list in 2 parts at index 'cut', and you swap the 2 parts, print the new list
list_part1 = original_list[:cut]
list_part2 = original_list[cut:]
new_list = list_part2 + list_part1

print(new_list)