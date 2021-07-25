

from program4.python_0210_practice_mrt_data_basic import line_name_dict
from collections import defaultdict
from itertools import permutations


# Let's assume, the passenger can maximum transit twice
# Let's list out all change lines possibilities

# So I am going to define a dict
# key - a tuple like ('blue_line', 'brown_line')
# value - all change line possibilities

change_line_possibilities_dict = defaultdict(list)


def populate_change_lines_possibilities_dict():

    # because the start station and end station can be of the same color
    # Let's build a list which each line appears twice.
    line_name_list = list(line_name_dict.keys()) * 2
    print(line_name_list)

    # Let's see how many possibilities there exist
    possible_set = set(permutations(line_name_list, 2))
    print(possible_set)


populate_change_lines_possibilities_dict()