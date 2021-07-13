from itertools import combinations

green_line = {'Pasir Ris', 'Tampines', 'Simei', 'Tanah Merah', 'Bedok', 'Kembangan', 'Eunos', 'Paya Lebar', 'Aljunied',
              'Kallang', 'Lavender', 'Bugis', 'City Hall', 'Raffles Place', 'Tanjong Pagar', 'Outram Park',
              'Tiong Bahru', 'Redhill', 'Queenstown', 'Commonwealth', 'Buona Vista', 'Dover', 'Clementi', 'Jurong East',
              'Chinese Garden', 'Lakeside', 'Boon Lay', 'Pioneer', 'Joo Koon', 'Gul Circle', 'Tuas Crescent',
              'Tuas West Road', 'Tuas Link'}
green_sub_line = {'Tanah Merah', 'Expo', 'Changi Airport'}

red_line = {'Jurong East', 'Bukit Batok', 'Bukit Gombak', 'Choa Chu Kang', 'Yew Tee', 'Kranji', 'Marsiling',
            'Woodlands', 'Admiralty', 'Sembawang', 'Canberra', 'Yishun', 'Khatib', 'Yio Chu Kang', 'Ang Mo Kio',
            'Bishan', 'Braddell', 'Toa Payoh', 'Novena', 'Newton', 'Orchard', 'Somerset', 'Dhoby Ghaut', 'City Hall',
            'Raffles Place', 'Marina Bay', 'Marina South Pier'}

yellow_line = {'Dhoby Ghaut', 'Bras Basah', 'Esplanade', 'Promenade', 'Nicoll Highway', 'Stadium', 'Mountbatten',
               'Dakota', 'Paya Lebar', 'MacPherson', 'Tai Seng', 'Bartley', 'Serangoon', 'Lorong Chuan', 'Bishan',
               'Marymount', 'Caldecott', 'Botanic Gardens', 'Farrer Road', 'Holland Village', 'Buona Vista',
               'one-north', 'Kent Ridge', 'Haw Par Villa', 'Pasir Panjang', 'Labrador Park', 'Telok Blangah',
               'HarbourFront'}
yellow_sub_line = {'Marina Bay', 'Bayfront', 'Promenade'}

purple_line = {'HarbourFront', 'Outram Park', 'Chinatown', 'Clarke Quay', 'Dhoby Ghaut', 'Little India', 'Farrer Park',
               'Boon Keng', 'Potong Pasir', 'Woodleigh', 'Serangoon', 'Kovan', 'Hougang', 'Buangkok', 'Sengkang',
               'Punggol'}

brown_line = {'Woodlands North', 'Woodlands', 'Woodlands South', 'Springleaf', 'Lentor', 'Mayflower', 'Bright Hill',
              'Upper Thomson', 'Caldecott', 'Mount Pleasant', 'Stevens', 'Napier', 'Orchard Boulevard', 'Orchard',
              'Great World', 'Havelock', 'Outram Park', 'Maxwell', 'Shenton Way', 'Marina Bay', 'Marina South',
              'Gardens by the Bay'}

lines_list = (green_line, green_sub_line, red_line, yellow_line, yellow_sub_line, purple_line, brown_line)

transit_stations = set()

comb = list(combinations(set(range(len(lines_list))), 2))

for i in range(len(comb)):
    lines_set_1 = lines_list[comb[i][0]]
    lines_set_2 = lines_list[comb[i][1]]
    inter = lines_set_1 & lines_set_2
    print(inter)
