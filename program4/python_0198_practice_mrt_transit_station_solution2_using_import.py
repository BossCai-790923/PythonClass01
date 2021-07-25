
from collections import defaultdict


from python_0196_practice_mrt_transit_station_solution1 import line_name_dict


station_to_lines_dict = defaultdict(set)

'''
--------------------------
Solution 2 Logic
--------------------------
I can use a similar data structure as in 196. But I use a more efficient way to find transit stations.
I can loop all stations of all lines, I handle those stations one by one.
I add the line name to the set which belongs to the station in the station_to_lines_dict 
So that I can avoid all those line combinations / set intersection code

I need to refactor the variable name to station_lines_dict, as it will include all stations.
'''

def populate_station_to_lines_dict():
    for line_name, line in line_name_dict.items():
        for station in line:
            station_to_lines_dict[station].add(line_name)


# MAIN PROGRAM BEGIN ==================================

# Step 1) Call the function
populate_station_to_lines_dict()

# pprint(station_to_lines_dict)

for station, lines in station_to_lines_dict.items():
    if len(lines) > 1:
        print(f"{station} is a transit station, which joins {lines}")