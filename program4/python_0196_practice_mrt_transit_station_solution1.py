'''
Introduction:
We are going to design a Singapore MRT transit app.
Right now, Singapore MRT system has green_line / red_line / yellow_line / purple_line / brown_line, 5 lines.
Green_line and yellow_line also have sub lines, meaning in total, we have 7 lines.

I've defined the 7 tuples as below:
'''


from collections import defaultdict
from itertools import combinations
from pprint import pprint


# PREPARE DATA BEGIN =================================

green_line= ('Pasir Ris', 'Tampines', 'Simei', 'Tanah Merah', 'Bedok', 'Kembangan', 'Eunos', 'Paya Lebar', 'Aljunied', 'Kallang', 'Lavender', 'Bugis', 'City Hall', 'Raffles Place', 'Tanjong Pagar', 'Outram Park', 'Tiong Bahru', 'Redhill', 'Queenstown', 'Commonwealth', 'Buona Vista', 'Dover', 'Clementi', 'Jurong East', 'Chinese Garden', 'Lakeside', 'Boon Lay', 'Pioneer', 'Joo Koon', 'Gul Circle', 'Tuas Crescent', 'Tuas West Road', 'Tuas Link')
green_sub_line= ('Tanah Merah', 'Expo', 'Changi Airport')

red_line= ('Jurong East','Bukit Batok','Bukit Gombak','Choa Chu Kang','Yew Tee','Kranji','Marsiling','Woodlands','Admiralty','Sembawang','Canberra','Yishun','Khatib','Yio Chu Kang','Ang Mo Kio','Bishan','Braddell','Toa Payoh','Novena','Newton','Orchard','Somerset','Dhoby Ghaut','City Hall','Raffles Place','Marina Bay','Marina South Pier')

yellow_line= ('Dhoby Ghaut', 'Bras Basah', 'Esplanade', 'Promenade', 'Nicoll Highway', 'Stadium', 'Mountbatten', 'Dakota', 'Paya Lebar', 'MacPherson', 'Tai Seng', 'Bartley', 'Serangoon', 'Lorong Chuan', 'Bishan', 'Marymount', 'Caldecott', 'Botanic Gardens', 'Farrer Road', 'Holland Village', 'Buona Vista', 'one-north', 'Kent Ridge', 'Haw Par Villa', 'Pasir Panjang', 'Labrador Park', 'Telok Blangah', 'HarbourFront')
yellow_sub_line= ('Marina Bay', 'Bayfront', 'Promenade')

purple_line= ('HarbourFront', 'Outram Park', 'Chinatown', 'Clarke Quay', 'Dhoby Ghaut', 'Little India', 'Farrer Park', 'Boon Keng', 'Potong Pasir', 'Woodleigh', 'Serangoon', 'Kovan', 'Hougang', 'Buangkok', 'Sengkang', 'Punggol')

brown_line = ('Woodlands North', 'Woodlands', 'Woodlands South', 'Springleaf', 'Lentor', 'Mayflower', 'Bright Hill', 'Upper Thomson', 'Caldecott', 'Mount Pleasant', 'Stevens', 'Napier', 'Orchard Boulevard', 'Orchard', 'Great World', 'Havelock', 'Outram Park', 'Maxwell', 'Shenton Way', 'Marina Bay', 'Marina South', 'Gardens by the Bay')

'''
Requirement: Your task is find out all the transit stations among all the lines.
'''


# 1) I want to give a number to each of the 7 lines
# The name and line are 1 to 1 mapping, so I use a dictionary to define it.
line_name_dict = {  'green_line'        : green_line,
                    'green_sub_line'    : green_sub_line,
                    'red_line'          : red_line,
                    'yellow_line'       : yellow_line,
                    'yellow_sub_line'   : yellow_sub_line,
                    'purple_line'       : purple_line,
                    'brown_line'        : brown_line}


# 2) I need a container to hold all transit stations.
# Each transit station will join at least 2 lines, meaning 1 transit station can map to more than 1 lines.
# So I define a dict here.
# key   : station name
# value : a set which holds all the lines which the transit station joins together.

# I will use defaultdict, which will automatically put a empty set when the key is not in the dict
transit_station_to_lines_dict = defaultdict(set)


def populate_transit_station_to_lines_dict():

    # Step 1) because I need to find all transit stations, meaning, I need to find all combination possibilities of any 2 lines
    line_combination_set = set(combinations(line_name_dict, 2))

    # Step 2) among all these 2 lines combinations, whether there are transition stations between them?

    # Solution:
    # Create line1_stations_set for all stations of line 1
    # Create line2_stations_set for all stations of line 2
    # See whether line1_stations_set and line2_stations_set intersection is empty or not.
    # If it is not empty, meaning there is at least 1 transit station between the 2 lines.

    for line1_name, line2_name in line_combination_set:
        line1_stations_set = set(line_name_dict[line1_name])
        line2_stations_set = set(line_name_dict[line2_name])
        transit_stations = line1_stations_set & line2_stations_set

        if len(transit_stations) > 0: # transit station exists between line1 and line2
            # print(f"{line1_name} - {line2_name}: {transit_stations}")

            for transit_station in transit_stations:

                # if I use a normal dict, I have to check whether transit_station in the dict or not, like this:
                # if transit_station not in transit_station_to_lines_dict:
                #     transit_station_to_lines_dict[transit_station] = set()

                transit_station_to_lines_dict[transit_station].add(line1_name)
                transit_station_to_lines_dict[transit_station].add(line2_name)



# MAIN PROGRAM BEGIN =======================================

populate_transit_station_to_lines_dict()
pprint(transit_station_to_lines_dict)
