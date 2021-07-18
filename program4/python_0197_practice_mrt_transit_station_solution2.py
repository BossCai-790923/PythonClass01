
from collections import defaultdict
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