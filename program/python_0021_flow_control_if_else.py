
years_learning_python = int(input("How many years have you been learning Python? "))


# IMPORTANCE !!! --------------------------------------------------
#
# if <boolean expression>:
#     <statement>
#     <statement>
#     <statement>
# else:
#     <statement>
#     <statement>
#
# 1) ":" at the end of the else clause
# 2) All code under else section are indented 4 spaces.
# 3) Treat the 2 print statements under else clause as a 'block', because they are indented 4 spaces.
#    The 'block' will be executed if years_learning_python > 5 is False, otherwise, the 'block' won't get executed.
# -----------------------------------------------------------------

# if years_learning_python == 5,
# then 5 > 5 is False.

if years_learning_python > 5:
    print(f"Not bad! {years_learning_python} years is quite a long time, you've already been a Python Guru!")
    print("I am sure you can earn a lot of money in the market!")
else:
    print(f"{years_learning_python} years is still quite short time.")
    print("I know it is hard, just hang in there! Not everybody has the opportunity to learn Python!")
    print("You are really lucky!")

print("Python is the future! You are on the right track!")