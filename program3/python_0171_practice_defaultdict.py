from collections import defaultdict



normal_dict = {}

for i in range(10):
    if i not in normal_dict:
        normal_dict[i] = 0
    normal_dict[i] += 1

print(normal_dict)

# without line 8 and 9, your program goes wrong immediately


default_dict = defaultdict(int)

for i in range(10):
    default_dict[i] += 1

print(default_dict)