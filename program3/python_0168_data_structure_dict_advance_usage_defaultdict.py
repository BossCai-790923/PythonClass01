number_count_dict = {
    '0': 0,
    '1': 0,
    '2': 0,
    '3': 0,
    '4': 0,
    '5': 0,
    '6': 0,
    '7': 0,
    '8': 0,
    '9': 0
}

# Python has a special dict - 'defaultdict' which is perfect for such scenario

# IMPORTANCE !!! -------------------------------------------
# How to use defaultdict?

# Step 1) import defaultdict from module collections
from collections import defaultdict

# Step 2) Create defaultdict object using defaultdict constructor, and pass in 'int' constructor to it.
# Meaning, if the key doesn't exist in the defaultdict, defaultdict will call the 'int' constructor to create a value, and insert the value for the key into the dictionary

defaultdict_int = defaultdict(int) # 'int' means int(). int() will create int 0

print(f"defaultdict_int size is {len(defaultdict_int)}")

for ch in '0123456789':
    print(f"key: {ch} is found in defaultdict_int with value: {defaultdict_int[ch]}")

print(f"defaultdict_int size is {len(defaultdict_int)}")

print(defaultdict_int)



# Example 2 --------------------------------------------------
print("Example 2: pass float constructor to defaultdict ------------------------")
defaultdict_float = defaultdict(float) # 'float' means float(). float() will create a float 0.0

for i in range(10):
    print(f"key: {i} is found in defaultdict_float with value: {defaultdict_float[i]}")

print(defaultdict_float)


# Example 3 --------------------------------------------------
print("Example 3: pass list constructor to defaultdict ------------------------")
defaultdict_list = defaultdict(list) # 'list' means list(). list() will create a empty list []

for i in range(10):
    print(f"key: {i} is found in defaultdict_list with value: {defaultdict_list[i]}")

print(defaultdict_list)


# Example 4 -------------------------------------------------
print("Example 4: pass your own non-arg function to defaultdict ---------------")

import random

def random_sqr():
    return random.randint(0, 10) ** 2

defaultdict_random_sqr = defaultdict(random_sqr) # 'random_sqr' means function random_sqr()

for i in range(10):
    print(f"key: {i} is found in defaultdict_random_sqr with value: {defaultdict_random_sqr[i]}")

print(defaultdict_random_sqr)


# Functional Programming -----------------------------------------------------------------------------------
# You treat function like a variable
# You pass function around
# Previously, only variable is the first citizen; and now we promote function to first citizen as well.
