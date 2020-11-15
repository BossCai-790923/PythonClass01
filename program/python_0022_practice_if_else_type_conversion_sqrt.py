'''
Requirement:
1) Ask user to input a number from Console
2) Then you need to tell whether the number is a square number or not
'''

#get user input
number_a = int(input("Plase input a number: "))


# Core logic ------------------------------
# 5 ** 2 = 25
# 5 ** 3 = 125
# 5 ** 4 = 625
# 25 ** (1/2) = 5
# 125 ** (1/3) = 5
# 625 ** (1/4) = 5
# -----------------------------------------
number_a_square_root = number_a ** (1/2)
print(f"{number_a}'s square root is {number_a_square_root}")

number_a_square_root_int = int(number_a_square_root)
print(f"After I convert {number_a_square_root} to integer, its value is {number_a_square_root_int}")

if number_a_square_root == number_a_square_root_int:
    print(f"Because {number_a_square_root} == {number_a_square_root_int}, so {number_a} is a square number.")
else:
    print(f"Because {number_a_square_root} != {number_a_square_root_int}, so {number_a} is NOT a square number.")


# Secret knowledge -------------------------------------
# Please try replace all
# {number_a_square_root}
# to
# {number_a_square_root:.2f}
#
# ':.2f' has 3 parts:
#
# :    means   I want to format this number
# .2   means   keep 2 digits after the decimal point .
# f    means   this is float number
# ------------------------------------------------------