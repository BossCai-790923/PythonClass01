#bool 布尔类型


# bool is the 4th data type in Python
# it has only 2 values. True and False
# it represents something True or False
# For example: is today a Sunny day? True
# For example: Is today Sunday? True
# For example: Is today Monday? False

#Step 1) define variables
bool1 = True
bool2 = False

#Step 2) Use variables
print('variable bool type is:', type(bool1), 'bool1 =', bool1)
print('variable bool type is:', type(bool2), 'bool2 =', bool2)
# built-in function type(): it tells you the type of some variable.
# Here, both bool1 and bool2 are of type 'bool'



# You can compare 2 values and you get a True/False result.
# The result is assigned to a variable whose type is bool.
# It is separated by '=', on the left is the variable name. on the right is a 'boolean expression'.
# What is a 'boolean expression'?
# 1 > 2 is a boolean expression, and the expression's value is False
# 100 < 200 is a boolean expression, and the expression's value is True
bool3 = (1 > 2)         # 1 > 2 is False. So bool3 is assigned a bool value -> False
bool4 = (100 < 200)     # 100 < 200 is True. So bool4 is assigned a bool value -> True
print('variable bool type is:', type(bool3), 'bool3 =', bool3)
print('variable bool type is:', type(bool4), 'bool4 =', bool4)


