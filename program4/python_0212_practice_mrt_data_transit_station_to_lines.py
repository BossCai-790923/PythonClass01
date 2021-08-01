

from python_0211_practice_mrt_data_station_to_lines import populate_station_to_lines_dict
from python_0211_practice_mrt_data_station_to_lines import station_to_lines_dict
from collections import defaultdict
from pprint import pprint

# PREPARE DATA BEGIN ======================================
transit_station_to_lines_dict = defaultdict(set)



# FUNCTION DEFINITION BEGIN ==========================
def populate_transit_station_to_lines_dict():

    # after I call the below function which is defined in 0211
    populate_station_to_lines_dict()

    # then the station_to_lines_dict which is defined in 0211 is fully populated.
    # Then I can iterate station_to_lines_dict one by one, to find all transit stations.
    for station, lines in station_to_lines_dict.items():
        if len(lines) > 1:
            transit_station_to_lines_dict[station] = lines


# MAIN PROGRAM BEGIN ===========================
# main program is for testing purpose

if __name__ == '__main__':

    # Step 1) call the function
    populate_transit_station_to_lines_dict()

    # Step 2) see the data
    pprint(transit_station_to_lines_dict)