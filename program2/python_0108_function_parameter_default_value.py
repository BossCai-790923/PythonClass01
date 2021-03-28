# IMPORTANTANCE !!! --------------------------------------------
# User can pass or not pass parameter border
# Parameter who has a default value should be put the last
# --------------------------------------------------------------
def banner(message, border='-'):
    '''
    This function creates a border for the supplied message

    :param message: to be surrounded by the border
    :param border: border format
    :return: nothing
    '''
    line = border * len(message)
    print(line)
    print(message)
    print(line)


banner("Singapore is a beautiful city")
banner("Happy Sunday!", "*")


'''
Requirement:
define a function. It can greet any user(parameter = name), with default message = 'Good morning'
'''