"""
Now you have 1000 tiles each from '0' to '9'.
If you start installing door number for '0001'.
Question: What's the maximum door number you can install till your run out of tiles?
A more challenging question:
Can you use defaultdict in this Question?
"""

counter = {
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


num_candidate = 0
enough = 1

while enough:
    str_candidate = f'{num_candidate:04d}'
    for i in range(4):
        counter[str_candidate[i]] += 1

    for key in counter:
        if counter[key] > 1000:
            enough = 0

    num_candidate += 1


print(f"The maximum door number you can install is {num_candidate}")

