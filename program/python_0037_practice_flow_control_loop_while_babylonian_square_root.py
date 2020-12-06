'''
Babylonian Square-root algorithm is very famous!
巴比伦算法

Here it is how it works to calculate the square root of any number x:

Step 1) define variable a = 1
Step 2) define variable b = x / a

Step 3) assign variable a = (a + b) / 2   - Now a stands in the mid point of a and b. This is to move a closer to b
Step 4) assign variable b = x / a

Because square_root * square_root = x; so a and b one is smaller than square_root, another is bigger than square_root
We move a to the mid point between a and b, so we make a closer to the square_root
because a * b = x, if a is closer to the square_root, b is also closer to the square_root

Step 5) assigne variable a = (a + b) /2
Step 6) assign variable b = x / a

Step 7) assigne variable a = (a + b) /2
Step 8) assign variable b = x / a

repeat ... repeat ...

Until a and b and close enough, say b - a < 0.0000000000000000000001
Then a is equal to b (almost)
Then a or b is the square root of x
'''

diff = 0.00000001

x = int(input("Number: "))

# define initial value
a = 1
b = x / a
actual_diff = b - a
print(f'a:{a}, b:{b}, actual_diff:{actual_diff}')


while actual_diff > diff:
    a = (a + b) / 2
    b = x / a

    #[Solution 1]
    actual_diff = abs(a - b)

    #[Solution 2]
    # actual_diff = (a - b) if a > b else (b - a)
    print(f'a:{a:.3f}, b:{b:.3f}, actual_diff:{actual_diff:.3f}')

print(f'Square root of {x} is : {a}')
print(f'{a} * {a} = {a ** 2}')



