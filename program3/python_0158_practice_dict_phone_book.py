# Requirment:
# Implement a simple database using dictionary.
# The dictionary uses person names as keys.
# Each person is represented as another dictionary with keys 'phone' and 'addr' referring to their phone number and address repectively.

people = {

    'Alice': {
        'phone': '2341',
        'addr': 'Foo drive 23'
    },

    'Beth': {
        'phone': '9012',
        'addr': 'Bar street 42'
    },

    'Cecil': {
        'phone': '2158',
        'addr': 'Baz avenue 90'
    }

}


labels = {
    'phone': 'phone number',
    'addr': 'address'
}

name = input("Name: ")
request = input("'Phone number (p) or address (a) ? ")


if request == 'p':
    key = 'phone'

if request == 'a':
    key = 'addr'

if name in people:
    print(f"{name}'s {labels[key]} is {people[name][key]}")
else:
    print("No such persons:", name)

# --------------------------------------------------------------------------------
# HOMEWORK: Please replace 'SOMETHING' at line 42 with a proper dictionary expression to let the program show the correct address or phone number for the request person
# --------------------------------------------------------------------------------


# ----------------
# Explanation:
# ----------------

# people is a dict, so you can put [name] after dict people -> people[name]
# This is accessing the value for key (stored in variable name) in the dict 'people'

# people is a nested dict, its value are dict as well, so people[name] is a dict as well, so can put [key] after dict 'people[name]' --> people[name][key]
# this is accessing the value for key (stored in variable key) in the dict people[name]


# ----------------
# Answer:
# ----------------
#     print(f"{name}'s {labels[key]} is {people[name][key]}")


# ----------------
# Wrong Answer:
# ----------------
#     print(f"{name}'s {labels[key]} is {people[name[key]]}")
#
# Why?
# Because Python program runs from top line to bottom line
# In the line, Python program runs from left word to right word.
# In the same word, Python program runs from inside to outside.
