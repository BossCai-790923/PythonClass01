'''
The Fibonacci sequence:

The Fibonacci sequence is a sequence of numbers such that any number, except for the first and second, is the sum of the previous two:
0, 1, 1, 2, 3, 5, 8, 13, 21...

Please tell me the number of the index n.

Requirement:
Write a function which accepts sequence index as argument, returns numbers in the fibonacci sequence

def fib(n):
    pass

fib(0) -> 0
fib(1) -> 1
fib(2) -> 1
fib(3) -> 2
... ...

'''


'''
1) the first 2 number are roots
2) I need 2 variables -> last & current


n          0     1          2            3       4 ...
fib(n)     0     1          1            2       3 ... 
           last  current 
                 last       current
                            last         current
                            

How to move the 2 variable to the right by 1 step? 
1) last = current
2) current = current + last (old)
'''


def fib(n):

    if n == 0:
        return 0

    if n == 1:
        return 1

    last = 0
    current = 1

    for i in range(n-1):
        last_old = last
        last = current
        current = last_old + current

    return current


'''
2 places can be optimized:
'''


def fib2(n):

    if n < 2:
        return n

    last = 0
    current = 1

    for _ in range(n-1):
        last, current = current, last + current

    return current




for i in range(20):
    print(fib2(i), end = ' ')