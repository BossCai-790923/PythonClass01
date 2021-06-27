'''
There is big resort, it has 2000 rooms.
Door number tiles need to be installed for all these 2000 rooms, starting from '0001' to '2000'.
Door number is composed of 4 tiles. i.e.
'0001' is composed of 3 '0' and 1 '1';
'2000' is composed of 3 '0' and 1 '2'.

Question:
How many tiles need to be prepared for number 0 - 9?
'''

# PREPARE DATA BEGIN -------------------------------------
number_count_dict = {}
for number in range(10):
    number_count_dict[number] = 0

print(number_count_dict)

# MAIN PROGRAM BEGIN ------------------------------------
# Using math to figure out the 4 digit of the door_number

for door_number in range(1, 2001):

    unit_digit = door_number % 10
    tens_digit = (door_number - unit_digit) // 10 % 10
    hundreds_digit = (door_number - tens_digit * 10 - unit_digit) // 100 % 10
    thousands_digit = (door_number - hundreds_digit * 100 - tens_digit * 10 - unit_digit) // 1000 % 10

    # print(thousands_digit, hundreds_digit, tens_digit, unit_digit)

    number_count_dict[unit_digit] += 1
    number_count_dict[tens_digit] += 1
    number_count_dict[hundreds_digit] += 1
    number_count_dict[thousands_digit] += 1

print(number_count_dict)