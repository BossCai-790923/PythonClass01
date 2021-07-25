
from python_0212_practice_mrt_data_transit_station_to_lines import populate_transit_station_to_lines_dict # Import a function
from python_0212_practice_mrt_data_transit_station_to_lines import transit_station_to_lines_dict # Import a dict
from collections import defaultdict
from pprint import pprint


# PREPARE DATA BEGIN ======================================
line_to_transit_stations_dict = defaultdict(set)

# FUNCTION DEFINITION BEGIN ===============================
def populate_line_to_transit_station_dict():

    # after I call function populate_transit_station_to_lines_dict which is defined in 0212
    populate_transit_station_to_lines_dict()

    # then the transit_station_to_lines_dict which is defined in 0212 is fully populated
    # then I can iterate transit_station_to_lines_dict one by one
    for station, lines in transit_station_to_lines_dict.items():
        for line in lines:
            line_to_transit_stations_dict[line].add(station)





# MAIN PROGRAM BEGIN ==================================
if __name__ == '__main__':

    # Step 1) call the function
    populate_line_to_transit_station_dict()

    # see the data
    pprint(line_to_transit_stations_dict)
