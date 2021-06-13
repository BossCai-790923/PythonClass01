
# Solution 1: Create a dict using {} ------------------------------------

car = {
    "brand": "BMW",
    "model": "X5",
    "year": 2021
}
print(car)


plane = {
    'name': "Boeing 787",
    'passenger': 330,
    'cruising_speed': 913,
    'maiden_flight': '15 Dec 2009',
    'wingspan': 60.1,
    'max_speed': 954
}
print(plane)


students = {
    1: "Tom",
    5: "Billy",
    10: 'Sandy',
    16: 'Sue'
}
print(students)

stock_prices = {
    "DBS": ('D05', 29.710, -0.110, -0.37),
    'Singtel': ('Z74', 2.380, -0.020, -0.83),
    'UOB': ('U11', 26.100, None, None),
}
print(stock_prices)

stupid_dict = {
    'a': 1,
    1: tuple("hello"),
    tuple("hello"): plane
}
print(stupid_dict)

# In summary:
# For key, you can use str / int / float / tuple. BUT YOU CANNOT USE LIST
# For value, you can use anything

# IMPORTANCE !!! ---------------------------------------------------------------------------------------------------------------
# You can use immutable value as the dict key.
# In our real life, key can't change it shape. Once key changes its shape, it can't open its lock
# So, you can't use list which is mutable as the dict key
# But for value, you can put anything. Value equals to the 'thing' inside the box which you can use the key to open
# ------------------------------------------------------------------------------------------------------------------------------


# Solution 2: Create a dict using dict constructor ------------------------------------
userNameAndAge = dict(Peter=38, John=51, Alex=13, Alvin='Unknown')
print(userNameAndAge)

a_man_list = [('name', 'Gumby'),('age', 42)]
a_man_dict = dict(a_man_list)
print(a_man_dict)

print('---------------------------------------------')

# HOMEWORK --------------------------------
# Do not run these code, tell me the output
# Tell me the output of the below code:
# print(stupid_dict['a'])
# print(stupid_dict[stupid_dict['a']])
# print(stupid_dict[stupid_dict[stupid_dict['a']]])
# --------------------------------------------------------------------
# Attention: This dict is REALLY STUPID, as you shouldn't use mix types of keys in a dictionary
# You can use mix types of keys, but you shouldn't.
# This is like: Can I stop a car on train tracks when no trains are coming? Yes you can, but you shouldn't.
# --------------------------------------------------------------------
