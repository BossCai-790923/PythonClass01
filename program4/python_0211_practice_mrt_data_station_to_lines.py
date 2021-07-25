
from python_0210_practice_mrt_data_basic import line_name_dict
from collections import defaultdict


# PREPARE DATA BEGIN =================================
station_to_lines_dict = defaultdict(set)


# FUNCTION DEFINITION BEGIN ==========================
def populate_station_to_lines_dict():
    for line_name, line in line_name_dict.items():
        for station in line:
            station_to_lines_dict[station].add(line_name)



# MAIN PROGRAM BEGIN ==================================
if __name__ == '__main__':

    populate_station_to_lines_dict()

    for station, lines in station_to_lines_dict.items():
        if len(lines) > 1:
            print(f"{station} is a transit station, which joins {lines}")