# example 1)

# Step 1) define a variable
toms_age = 20

# Step 2) I use the variable toms_age
# ==  tells you whether the number on the left and right are equal or not
# =   assign value on right to the variable on the left
#     'toms_age == 20' is a boolean expression, and its value is True
print("Is Tom 20 years old?", toms_age == 20)

print("Is Tom 13 years old?", toms_age == 13) # False
print("Tom is not 20 years old. Right?", toms_age != 20) # False


a = (toms_age == 20) # toms_age == 20 equals to True. So variable a equals to True
b = (toms_age == 13) # toms_age == 13 equals to False. So variable b equals to False
c = (toms_age != 20) # Variable c equals to False
d = (toms_age != 13) # Variable d equals to True
e = (toms_age < 20) # Variable e equals to False
f = (toms_age <= 20) # Variable f equals to True
g = (toms_age > 20) # Variable e equals to False
h = (toms_age >= 20) # Variable f equals to True
print(a,b,c,d,e,f,g,h) # True False False True False True False True



# assign operator (=) has a lower priority then th 6 rational operator(>  <  >=  <=  !=  ==)
# So the 6 rational operators always go before the assign operator.
# This is really a good example how to write rubbish code
# Remember: your program is like a composition. It is for people to READ.
# That is why, python is called a programming 'LANGUAGE'. Its purpose is to communicate with other people, rarely with computer.
# So your program must be easily understandable.
a = toms_age == 20 # toms_age == 20 equals to True. So variable a equals to True
b = toms_age == 13 # toms_age == 13 equals to False. So variable b equals to False
c = toms_age != 20 # Variable c equals to False
d = toms_age != 13 # Variable d equals to True
e = toms_age < 20 # Variable e equals to False
f = toms_age <= 20 # Variable f equals to True
g = toms_age > 20 # Variable e equals to False
h = toms_age >= 20 # Variable f equals to True


# example 2)
my_math_mark = 75
is_my_math_excellent = (my_math_mark > 90)
print("Is my math excellent?", is_my_math_excellent)

have_i_failed_in_math = (my_math_mark < 60)
print("Have I failed in math?", have_i_failed_in_math)

billy_math_mark = 75
does_billy_have_same_score_as_mine = (my_math_mark == billy_math_mark)
print("Does Billy have the same math score as mine?", does_billy_have_same_score_as_mine)


#----------------------------------------
# You must remember:
# the meaning of
# ==
# !=
# <
# <=
# >
# >=
#----------------------------------------







