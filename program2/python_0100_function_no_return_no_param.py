'''
We used to say: define a variable, use a variable
Now we say: define a function, call a function
'''

# Part 1) define a function: greet_user() --------------------------
#
# def          : keyword. Every time you define a function, you start with 'def'.
# greet_user   : function name. Just like variable name. Important: function name must be meaningful.
# ()           : parentheses.
# :            : Just like you use ":" at the end of a for range loop, it begins your function body.
def greet_user():
    '''
    Display a simple greeting.
    This part is called 'docstring'.
    It tells you what the function does.
    If you move your mouse over the function name, you can see docstring appear.
    :return:
    '''
    print("Hello!")
    print("What a nice day!")
    print("Nice to meet you on this beautiful weekend morning!")
    print("Any plan today? I wish you have a good rest. After all, tomorrow is Monday again.")


# Part 2) call a funtion: greet_user() ------------------------------
greet_user()
greet_user()
greet_user()
greet_user()
greet_user()

# Another example -------------------------

def launch_missile():
    '''
    This function will launch a missile.
    '''
    print("Missile launched!")


launch_missile()
launch_missile()
launch_missile()