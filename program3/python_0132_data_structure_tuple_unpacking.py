def unpacking_example():
    student_info = ('John', 'T0112233E', 'Oct 10th, 2007', 'Male')


    '''
    It looks like, ungroup student_info, assign its value to multiple variables.
    Actually, what happens is:
    On the left side, it is a tuple, which contains 4 values - name, ic, birthday, gender
    On the right side, it is tuple student_info 
    So this is assigning a tuple's value to the tuple on the left
    So after this, name, ic, birthday, gender will have the tuple student_info's value
    '''
    name, ic, birthday, gender = student_info
    print(name, ic, birthday, gender)

    # So this actually equals to
    (name, ic, birthday, gender) = student_info
    print(name, ic, birthday, gender)

'''
Summary:
tuple unpacking means:
1) Assign right tuple's value to the left tuple.
2) Left tuple is composed of variables.
3) So those variable will have the right tuple's values.
This equals to: you ungroup a tuple, and assign its value to multiple variables.
'''


def unpacking_example2():
    x = 'jelly'
    y = 'bean'

    # Create a tuple on the right
    # Assigne the tuple's value to the tuple on the left
    # So x has y's value, y has x's value
    x, y = y, x
    print(x, y) # bean jelly

    # it equals to
    (x, y) = (y, x)
    print(x, y) # jelly bean


def unpacking_example3():
    # This is again, assgin tuple on the right to the tuple on the left
    (a, (b, (c, d))) = (4, (3, (2, 1)))
    print(a, b, c, d) #4, 3, 2, 1

    # Because the outer most parentheses can be removed, so it equals to
    a, (b, (c, d)) = 4, (3, (2, 1))
    print(a, b, c, d) #4, 3, 2, 1




# unpacking_example()
# unpacking_example2()
unpacking_example3()