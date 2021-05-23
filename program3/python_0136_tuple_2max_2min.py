'''
Requirement:
Find the 2 maximum and 2 minimum values of the test_tup, and create a new tuple from the 4 values.
'''

test_tup = (5, 20, 3, 7, 6, 8, 45, 16)

def enumerate_example():
    sorted_list = sorted(test_tup) # sorted function will create a new list using test_tup's value.

    for index, value in enumerate(sorted_list): # revise 0069
        print(index, value)

    print('-' * 50)


#enumerate returns a list of tuples.
def enumerate_example2():
    sorted_list = sorted(test_tup) # sorted function will create a new list using test_tup's value.

    for item in enumerate(sorted_list): # revise 0069
        print(f"{item}. Its type is {type(item)}")
        index, value = item # tuple unpacking
        print(index, value)

    print('-' * 50)

# Solution 1) sorted and loop --------------------------------------

def solution1():
    result_list = []
    sorted_list = sorted(test_tup)
    for index, value in enumerate(sorted_list):
        if index < 2 or index > len(sorted_list) - 3:
            result_list.append(value)

    result_tuple = tuple(result_list)
    print(result_tuple)

    print('-' * 50)


# Solution 2) sorted and slicing ------------------------------------
def solution2():
    sorted_list = sorted(test_tup)
    result_tuple = tuple(sorted_list[:2] + sorted_list[-2:])
    print(result_tuple)




# enumerate_example()
# enumerate_example2()
# solution1()
solution2()


