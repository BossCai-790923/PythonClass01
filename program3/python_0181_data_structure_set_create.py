def using_curly_braces():
    set1 = {1, 2, 3, 4, 5}
    print("set1 = ", set1)
    print("set1 is a ", type(set1))
    print('-------------------------------------')

    dict1 = {}
    print('{} is a ', type(dict1))
    print('-------------------------------------')


def using_set_constructor_from_list_tuple_range_str():
    # create an empty set
    set2 = set()
    print("set2 = ", set2)
    print('-------------------------------------')

    # create a set using a list
    a_list = [1, 1, 2, 2, 3, 3]
    set3 = set(a_list)
    print("set3 = ", set3)

    set4 = set([1, 1, 2, 2])
    print("set4 = ", set4)
    # the square brackets inside belong to the list
    # The parentheses outside belong to the set constructor
    print('-------------------------------------')

    # create a set using a tuple
    set5 = set((1, 1, 2, 2))
    print("set5 = ", set5)
    # the parentheses inside belong to the tuple
    # The parentheses outside belong to the set constructor
    print('-------------------------------------')

    # create a set using a range
    range1 = range(1, 10)
    set6 = set(range1)
    print("set6 = ", set6)
    print('-------------------------------------')

    # create a set using a str
    set7 = set("Hello Python!")
    print("set7 = ", set7)
    print('-------------------------------------')

    # IMPORTANCE !!! -----------------------------------
    # 1) set is unordered
    # 2) duplicate value are only kept ONCE: there is only one 'l' and one 'o'
    # --------------------------------------------------



def using_set_construtor_from_dict():
    dict1 = {1:'a', 2:'b', 3:'c'}

    # remember when we loop a dictionary, we are actually looping its keys
    # So when we create a new set from a dictionary, we are actually creating a new set from the dictionary's keys as well.
    set8 = set(dict1)
    print(f"set(dict1) gives you a set with dict1's keys: {set8}")

    # Similarly, you can create a new set from a dictionary's values
    set9 = set(dict1.values())
    print(f"set(dict1.values()) gives you a set with dict1's values: {set9}")

    # Similarly, you can create a new set from a dictionary's items which are key / value pairs.
    set10 = set(dict1.items())
    print(f"set(dict1.items()) gives you a set with dict1's key / value pairs: {set10}")




# using_curly_braces()
# using_set_constructor_from_list_tuple_range_str()
using_set_construtor_from_dict()


# IMPORTANCE !!! -----------------------------------
#
# You can put an 'iterable' object into the set constructor -> set()
# What is an 'iterable' object?
# list  is iterable     because     for e in a_list:
# tuple is iterable     because     for e in a_tuple:
# range is iterable     because     for i in range(10):
# str   is iterable     because     for ch in "hello":
# dict  is iterable     because     for key in a_dict:
#                                   for value in a_dict.values():
#                                   for key, value in a_dict.items():
#
# What is an 'iterable' object?
# An iterable object is capable of returning its members one by one.
# An iterable object is anything that you can loop over with a for loop.
# ---------------------------------------------------



# HOMEWORK ------------------------------------------
# Create another 5 set from your daily life using all kinds of data / method
# Put int / float / bool / tuple
# Use set()
# ---------------------------------------------------