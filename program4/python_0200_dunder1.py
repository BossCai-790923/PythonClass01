'''
__name__ variable is a special python variable: python reserved variable
There are Double UNDERscore in the front and end.
Such variable has a special name in Python - dunder variable

Here is what happens:
As soon as your python program starts, either you run it directly, or it is imported indirectly
Python will assign a value to variable __name__, its value depends on how your python program is used

if you run it directly:  __name__ = '__main__'
if it is imported:       __name__ = file name
'''


def hello(name):
    print("Hello", name)


# MAIN PROGRAM BEGIN =======================================

if __name__ == '__main__':
    hello("Tom")
    print(f"variable '__name__' has value {__name__}")
