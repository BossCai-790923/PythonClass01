

from python_0210_practice_mrt_data_basic import line_name_dict
from python_0213_practice_mrt_data_line_to_transit_stations import *
from collections import defaultdict
from itertools import permutations
from pprint import pprint


# Let's assume, the passenger can maximum transit twice
# Let's list out all change lines possibilities


# PREPARE DATA BEGIN ======================================

# So I am going to define a dict
# key - a tuple like ('blue_line', 'brown_line')
# value - all change line possibilities

change_line_possibilities_dict = defaultdict(list)


# FUNCTION DEFINITION BEGIN ===============================

def populate_change_lines_possibilities_dict():

    # because the start station and end station can be of the same color
    # Let's build a list which each line appears twice.
    line_name_list = list(line_name_dict.keys()) * 2
    # print(line_name_list)

    # Let's see how many possibilities there exist
    possible_set = set(permutations(line_name_list, 2))
    # print(possible_set)

    for start_line, stop_line in possible_set:

        # among all these possibilities, there are 2 situations

        # situation 1) start line and stop line are on the same line
        if start_line == stop_line:

            # transit 0 times
            change_line_possibilities_dict[start_line, stop_line].append([start_line])

            # transit once is impossible

            # transit twice
            for transit_line in line_name_dict.keys():

                if transit_line == start_line:
                    continue

                start_line_transit_stations_set = line_to_transit_stations_dict[start_line]
                transit_line_transit_stations_set = line_to_transit_stations_dict[transit_line]
                common_transit_station_set = start_line_transit_stations_set & transit_line_transit_stations_set
                if len(common_transit_station_set) <= 1:
                    continue

                change_line_possibilities_dict[start_line, stop_line].append([start_line, transit_line, stop_line])


        # situation 2) start line and stop line are on different lines
        else:

            start_line_transit_stations_set = line_to_transit_stations_dict[start_line]
            stop_line_transit_stations_set = line_to_transit_stations_dict[stop_line]
            common_transit_stations_between_start_line_stop_line_set = start_line_transit_stations_set & stop_line_transit_stations_set


            # transit 0 time is impossible
            # transit once - there should exist at least 1 transit station between the 2 lines
            if len(common_transit_stations_between_start_line_stop_line_set) > 0:
                change_line_possibilities_dict[start_line, stop_line].append([start_line, stop_line])

            # transit twice
            for transit_line in line_name_dict.keys():

                if transit_line == start_line or transit_line == stop_line:
                    continue

                transit_line_transit_stations_set = line_to_transit_stations_dict[transit_line]

                common_transit_stations_between_start_line_transit_line_set = start_line_transit_stations_set & transit_line_transit_stations_set
                if len(common_transit_stations_between_start_line_transit_line_set) < 1:
                    continue

                common_transit_stations_between_stop_line_transit_line_set = stop_line_transit_stations_set & transit_line_transit_stations_set
                if len(common_transit_stations_between_stop_line_transit_line_set) < 1:
                    continue

                if common_transit_stations_between_start_line_transit_line_set == common_transit_stations_between_stop_line_transit_line_set and len(common_transit_stations_between_stop_line_transit_line_set) == 1:
                    continue

                change_line_possibilities_dict[start_line, stop_line].append([start_line, transit_line, stop_line])







# MAIN PROGRAM BEGIN =================================

if __name__ == '__main__':
    populate_line_to_transit_station_dict()
    populate_change_lines_possibilities_dict()
    pprint(change_line_possibilities_dict)