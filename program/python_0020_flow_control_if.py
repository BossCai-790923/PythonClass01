# Every python program we've seen so far is sequential exection.
# Code is executed strictly line after line, from top to bottom.

# Flow Control can help you skip over some lines of the code.


# if statement

today = input("What day is today?")

print('I get up at 7 am.')
print('I have my breakfast at 8 am.')


# IMPORTANCE !!! --------------------------------------------------
#
# if <boolean expression>:
#     <statement>
#     <statement>
#     <statement>
#
# 1) ":" at the end of the if clause
# 2) All code under if section are indented 4 spaces.
# 3) Treat the 3 print statements as a 'block', because they are indented 4 spaces.
#    The 'block' will be executed if today == 'Sunday' is True, otherwise, the 'block' won't get executed.
# -----------------------------------------------------------------


if today == 'Sunday': # today == 'Sunday' is a boolean expression. The boolean expression will always have a bool value - True / False
    print("I attend Mr Fan's Python lesson at 9 am.")
    print("I start working on my homework at 10:30 am.")
    print("Homework is done at 11:30 am.")

print("I have my lunch at 12 pm.")
print("I play football with my friends at 5 pm.")
print("I have my dinner at 7 pm.")
print("I go to bed at 10 pm.")

