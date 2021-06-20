dict1 = {'A':80, 'B':95}
dict2 = {'B':90, 'C':95}

'''
Requirement:
I have 2 dict - dict1 & dict2.
I want to merge dict2 into dict1, then dict1 and dict2 becomes 1 dict.
Possibly, some key / value pair in dict2 will override those in dict1
'''


print(f"Original dict1: {dict1}") # Original dict1: {'A': 80, 'B': 95}

# Solution 1 ------------------------------
# for key, value in dict2.items():
#     dict1[key] = value

# Solution 2 ------------------------------
dict1.update(dict2)


print(f"New dict1: {dict1}") # New dict1: {'A': 80, 'B': 90, 'C': 95}

