# The most important thing in Python programming is:
# 1) define a variable
# 2) use a variable


# this is defining a variable
# I can give the variable name whatever I want
# I want to give my variable a name -> a_number, and I want to put value 5 into variable a_number's box
a_number = 5

# I want to give my variable a name -> another_number, and I want to put value 2 into variable another_number's box
another_number = 2

# I want to give my variable a name -> greeting_word, and I want to put value 'Hello!' into variable greeting_word's box
greeting_word = 'hello!'


# Use variables
# print(a_number)
# print(another_number)
# print(greeting_word)

# Print 3 variables in one print command
# print(a_number, another_number, greeting_word)


plus_variable = a_number + another_number
minus_variable = a_number - another_number
multiply_variable = a_number * another_number
divide_variable = a_number / another_number         # 2.5     5 / 2 = 2.5

divide_variable2 = a_number // another_number       # 2       5 // 2 = 2 r 1
remainder_variable = a_number % another_number       # 1
power_variable = a_number ** another_number          # 5^2    5 * 5 = 25


# convert a line of code to comment: Ctrl + /
# print(plus_variable, minus_variable, multiply_variable, divide_variable, divide_variable2, remainder_variable, power_variable)

print(a_number, '+', another_number, '=', plus_variable)
print(a_number, '-', another_number, '=', minus_variable)
print(a_number, '*', another_number, '=', multiply_variable)
print(a_number, '/', another_number, '=', divide_variable)
print(a_number, '//', another_number, '=', divide_variable2)
print(a_number, '%', another_number, '=', remainder_variable)
print(a_number, '**', another_number, '=', power_variable)


a = 1
b = 2
c = 5
d = 6
e = 7
f = 9

answer = (a - (a / d) * (b / c)) / (e / f)
print(answer)