'''
There is big resort, it has 2000 rooms.
Door number tiles need to be installed for all these 2000 rooms, starting from '0001' to '2000'.
Door number is composed of 4 tiles. i.e.
'0001' is composed of 3 '0' and 1 '1';
'2000' is composed of 3 '0' and 1 '2'.

Question:
How many tiles need to be prepared for number 0 - 9?
'''

# PREPARE DATA BEGIN -----------------------------------

from collections import defaultdict

number_count_dict = defaultdict(int)

# shortcut key ---------------------------------
# block editing - Shift + Alt + Insert
# ----------------------------------------------


# MAIN PROGRAM BEGIN ------------------------------------

for door_number in range(1,2001):

    # Step 1) Calculate tile '0' count in front of door_number when its digit count is not 4
    if door_number < 10:
        number_count_dict['0'] += 3
    elif door_number < 100:
        number_count_dict['0'] += 2
    elif door_number < 1000:
        number_count_dict['0'] += 1

    # Step 2) Convert the door_number to str, so that I can loop the str by its digit, handle the digit one by one
    for tile in str(door_number):
        number_count_dict[tile] += 1

print(number_count_dict)