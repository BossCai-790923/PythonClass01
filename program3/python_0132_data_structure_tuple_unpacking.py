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




unpacking_example()