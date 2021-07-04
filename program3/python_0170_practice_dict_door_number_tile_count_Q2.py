'''
Now you have 1000 tiles each from '0' to '9'.
If you start installing door number for '0001'.
Question: What's the maximum door number you can install till your run out of tiles?


A more challenging question:
Can you use defaultdict in this Question?
'''


# PREPARE DATA BEGIN ========================================

# Step 1) Create a defaultdict with default value 10000

from collections import defaultdict

def init_tile_count():
    return 1000

tile_count = defaultdict(init_tile_count)

door_number = 1

# MAIN PROGRAM BEGIN =======================================

# Step 1) Use while True loop, to mimic installing door number, at the same time, we decrease the tile count from defaultdict

while True:

    if door_number < 10:
        tile_count['0'] -= 3

    elif door_number < 100:
        tile_count['0'] -= 2

    elif door_number < 1000:
        tile_count['0'] -= 1

    for tile in str(door_number):
        tile_count[tile] -= 1

    door_number += 1

    for key, value in tile_count.items():
        if value < 0:
            print(f"I've run out of the tile {key} when I paste door number {door_number}")
            exit()





