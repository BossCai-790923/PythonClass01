from python_0213_practice_mrt_data_line_to_transit_stations import *
from python_0214_practice_mrt_transit_possibilities import *
from python_0211_practice_mrt_data_station_to_lines import *



# FUNCTION DEFINITION BEGIN ============================

def find_1_line_route(line_name, start_station, end_station):
    line = line_name_dict[line_name]
    start_line_index = line.index(start_station)
    end_line_index = line.index(end_station)
    if start_line_index > end_line_index:
        possible_route = line[end_line_index:start_line_index+1]
        possible_route = possible_route[::-1]
    else:
        possible_route = line[start_line_index:end_line_index+1]
    return possible_route


def find_2_line_route(start_station_line_name, end_station_line_name, start_station, end_station):
    possible_route_list = []
    same_transit_station_set = line_to_transit_stations_dict[start_station_line_name] & line_to_transit_stations_dict[end_station_line_name]
    for transit_station in same_transit_station_set:
        part_1_route = find_1_line_route(start_station_line_name, start_station, transit_station)
        part_2_route = find_1_line_route(end_station_line_name, transit_station, end_station)
        route = part_1_route + part_2_route[1::]
        possible_route_list.append(route)

        # if len(route) == len(set(route)):
    return possible_route_list




def find_3_line_route(start_station_line_name, transit_station_line_name, end_station_line_name, start_station, end_station):
    possible_route_list = []
    same_transit_station_between_start_line_and_transit_line_set = line_to_transit_stations_dict[start_station_line_name] & line_to_transit_stations_dict[transit_station_line_name]
    same_transit_station_between_transit_line_and_end_line_set = line_to_transit_stations_dict[end_station_line_name] & line_to_transit_stations_dict[transit_station_line_name]

    for transit_station1 in same_transit_station_between_start_line_and_transit_line_set:
        for transit_station2 in same_transit_station_between_transit_line_and_end_line_set:
            part_1_route = find_1_line_route(start_station_line_name, start_station, transit_station1)
            part_2_route = find_1_line_route(transit_station_line_name, transit_station1, transit_station2)
            part_3_route = find_1_line_route(end_station_line_name, transit_station2, end_station)
            route = part_1_route + part_2_route[1::] + part_3_route[1::]

            if len(route) == len(set(route)):
                possible_route_list.append(route)

    return possible_route_list



# PREPARE DATA BEGIN =================================

# Read 'Start' station and 'End' station from passenger
start_station = input("Start station: ")
end_station = input("End station: ")

# There are multiple possible routs from start_station to end_station
possible_route_set = set()

# MAIN PROGRAM BEGIN =================================



if __name__ == '__main__':

    # Step 1) Populate all the dictionaries we prepared in our previous lessons -----------------
    populate_line_to_transit_station_dict()
    populate_change_lines_possibilities_dict()

    # Step 2) As each station can possibly be on more than 1 line.
    # So we have to use nested loop to see all the start_line and end_line combinations possibilities

    # For example, when passenger travels from 'Bishan' which is on red_line and yellow_line
    #                                       to 'Little India' which is on purple_line and blue_line
    # You can say, the passenger travels from
    # 1) red_line to purple_line
    # 2) red_line to blue_line
    # 3) yellow_line to purple_line
    # 4) yellow_line to blue_line
    # For each situation above, change_line_possibilities_dict (calculated in 0214) can tell you all the change line possibilities
    # We need to check one by one


    for start_line in station_to_lines_dict[start_station]:
        for end_line in station_to_lines_dict[end_station]:
            for line_list in change_line_possibilities_dict[start_line, end_line]:

                if len(line_list) == 1:
                    possible_route = find_1_line_route(line_list[0], start_station, end_station)
                    possible_route_set.add(possible_route)

                if len(line_list) == 2:
                    possible_route_list = find_2_line_route(line_list[0], line_list[1], start_station, end_station)
                    possible_route_set.update(possible_route_list)

                if len(line_list) == 3:
                    possible_route_list = find_3_line_route(line_list[0], line_list[1], line_list[2], start_station, end_station)
                    possible_route_set.update(possible_route_list)


    for possible_route in possible_route_set:
        print(f"{len(possible_route) - 1} stops in total: { ' -> '.join(possible_route) } " )