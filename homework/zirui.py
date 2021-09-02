index = [1, 0, 0]
swaps = input()
swaps = list(swaps)
for i in swaps:
    if i == 'A':
        swapped = index.pop(0)
        index.insert(1, swapped)
    if i == 'B':
        swapped = index.pop(1)
        index.insert(2, swapped)
    if i == 'C':
        swapped = index.pop(2)
        index.insert(0, swapped)
        swapped = index.pop(1)
        index.insert(2, swapped)
print(index.index(1)+1)