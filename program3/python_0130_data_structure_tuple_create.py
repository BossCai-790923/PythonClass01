'''
-----------------------
tuple
-----------------------
tuple is highly-similar to list.

Differences between tuple and list:

1) list is mutable, tuple is immutable.
   Once a tuple is created, you cannot change it.

2) you use [] in list, you use () in tuple
'''

def create_tuple_example():

    print('empty tuple and empty list ------------------------')
    tup_empty = ()
    list_empty = []
    print(tup_empty)
    print(list_empty)

    print("single value tuple and list ----------------------")
    tup_1 = (50,) # comma is mandatory as (50) is the same as 50
    list_1 = [50]
    print(tup_1)
    print(list_1)

    int_var = (50)
    print(type(int_var))

    print("multiple value tuple and list ---------------------")
    tup_multiple = (1, 2, 3, 4, 5)
    list_multiple = [1, 2, 3, 4, 5]
    print(tup_multiple)
    print(list_multiple)

    list_multiple[0] = -1
    print(list_multiple)
    # tup_multiple[0] = -1  # TypeError: tuple is immutable
    # print(tup_multiple)



create_tuple_example()