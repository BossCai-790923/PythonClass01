

'''
------------------------------
Pass Information to a function
------------------------------
Q) What is inside function parentheses?
A) You can define a variable which is only valid inside the function body.
   So here, you learn another way to define variable.

Q) What is Parameter?
A) Because the variable is ONLY valid inside the function body, so the variable has a special name - parameter

Q) Who will assign value to the variable(the parameter)?
A) When you call the function, you pass the value to the function call.


'''

# Part 1) define a function: greet_user(username) -------------------------------------------
def greet_user(username):
    '''
    Greet user, greet the specified user.
    :param username: who you will greet
    :return: nothing
    '''
    print(f"Hello, {username}!")
    print("What a nice day!")
    print("Nice to meet you on this beautiful weekend morning!")
    print("Any plan today? I wish you have a good rest. After all, tomorrow is Monday again.")



# Part 2) call a function: greet_user(username) ----------------------------------------------
greet_user('Tom')
greet_user('Billy')
greet_user('Sandy')

'''
Q) What is argument? 
A) When you call the function greet_user('Tom'), you put a str value 'Tom' in the pair of parentheses
   We say, you 'pass' value 'Tom' to the function greet_user('Tom')
   When the control goes inside the function body, this str value 'Tom' becomes the value of the parameter(variable) 'username'
   
   Here, 'Tom' has a special name - argument
'''