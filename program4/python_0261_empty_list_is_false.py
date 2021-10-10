
'''

The following values are treated as False:
empty list / empty tuple / empty dict / empty str / 0

The following values are treated as True:
non-empty list / non-empty tuple / non-empty dict / non-empty str / non 0

'''

# PREPARE DATA BEGIN =============================

empty_list = list()
empty_tuple = tuple()
empty_dict = dict()
empty_str = ''
int_0 = 0

non_empty_list = ['hello']
non_empty_tuple = ('python',)
non_empty_dict = {'hello':'python'}
non_empty_str = 'hello python'
non_int_0 = -1


# PREPARE FUNCTION BEGIN =========================

def true_or_false(*value_tuple):

    for value in value_tuple:

        if value: # this is the interesting part!
            print(f"{value} is True")
        else:
            print(f"{value} is False")

    print('-' * 50)


# MAIN PROGRAM BEGIN =========================
if __name__ == '__main__':
    true_or_false(empty_list, empty_tuple, empty_dict, empty_str, int_0)
    true_or_false(non_empty_list, non_empty_tuple, non_empty_dict, non_empty_str, non_int_0)




