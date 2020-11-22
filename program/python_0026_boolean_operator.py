print("'and' rule -------------------------------------")
print(f'"True and True" is {True and True}') # True
print(f'"True and False" is {True and False}') # False
print(f'"False and True" is {False and True}') # False
print(f'"False and False" is {False and False}') # False


print("'or' rule -------------------------------------")
print(f'"True or True" is {True or True}') # True
print(f'"True or False" is {True or False}') # True
print(f'"False or True" is {False or True}') # True
print(f'"False or False" is {False or False}') # False

print("'not' rule -------------------------------------")
print(f'"not True" is {not True}') # False
print(f'"not False" is {not False}') # True


bool_a = True
bool_b = False
bool_c = True
bool_d = False


# and - any value is False, then whole boolean expression is False
print(bool_a and bool_b and bool_c and bool_d) # False

# or - any value is True, then whole boolean expression is True
print(bool_a or bool_b or bool_c or bool_d) # True


# or - lowest priority, so it equals to
# bool_a and bool_b            or             bool_c and bool_d
print(bool_a and bool_b or bool_c and bool_d) # False



# So you use parenthesis () to change to evaluation order, so this equals to
# bool_a       and      (bool_b or bool_c)       and       bool_d
print(bool_a and (bool_b or bool_c) and bool_d) # False


# not - highest priority, so it equals to
# bool_a       and      (bool_b or bool_c)       and       not bool_d
print(bool_a and (bool_b or bool_c) and not bool_d) # True




