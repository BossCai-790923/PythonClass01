from program4.python_0210_practice_mrt_data_basic import line_name_dict
from collections import defaultdict
from itertools import permutations

possible_transit_set = set()
remove_from_set = set()
pts = set()


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

    print(">>>>>>")
    for lines in possible_set:
        for lines_2 in possible_set:
            if lines_2[0] == lines[0] or lines_2[1] == lines[0]:
                possible_transit_set.add(lines_2)
            if lines_2[0] == lines[1] or lines_2[1] == lines[1]:
                possible_transit_set.add(lines_2)
            for lines_3 in possible_transit_set:
                pts = possible_transit_set.copy()
                for lines_4 in possible_transit_set:

                    if lines_4[0] != lines_3[0] and lines_4[1] != lines_3[0]:
                        print(pts)
                        pts.remove(lines_4)
                    if lines_4[0] != lines_3[1] and lines_4[1] != lines_3[1]:
                        print(pts)
                        pts.remove(lines_4)
        print(pts)
        possible_transit_set.clear()


populate_change_lines_possibilities_dict()