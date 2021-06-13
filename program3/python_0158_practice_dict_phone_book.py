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
    print(f"{name}'s {labels[key]} is SOMETHING")
else:
    print("No such persons:", name)

# --------------------------------------------------------------------------------
# HOMEWORK: Please replace 'SOMETHING' at line 42 with a proper dictionary expression to let the program show the correct address or phone number for the request person
# --------------------------------------------------------------------------------
