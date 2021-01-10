animals = ['tiger', 'elephant', 'snake', 'shark'] * 2
print(animals) # ['tiger', 'elephant', 'snake', 'shark', 'tiger', 'elephant', 'snake', 'shark']

# Solution 1: Use del - remove item by index
del animals[1]
print(animals) # ['tiger', 'snake', 'shark', 'tiger', 'elephant', 'snake', 'shark']


# Solution 2: Use pop - remove item by index
# pop() returns the popped item
popped_animal = animals.pop() # it will pop out the last item from the list
print(popped_animal, 'is popped out.') # shark is popped out.
print(animals) # ['tiger', 'snake', 'shark', 'tiger', 'elephant', 'snake']

popped_animal = animals.pop(1)
print(popped_animal, 'is popped out at index 1.') # snake is popped out at index 1.
print(animals) # ['tiger', 'shark', 'tiger', 'elephant', 'snake']

# index must be a valid value, otherwise: error!
# IndexError: pop index out of range
# popped_animal = animals.pop(20)

# So you need to check index value before calling pop method
index = 20
if 0 <= index < len(animals):
    popped_animal = animals.pop(index)
    print(popped_animal, 'is popped out.')
    print(animals)
else:
    print(f"{index} is an invalid value for list animals. Right now we only have {len(animals)} items in animals list.")
# IMPORTANCE!!! ----------------------------------------------------
# built-in fuction: len(list) tells you the size of the list
# ------------------------------------------------------------------



# Solution 3: Use remove - remove item by value
animals.remove('tiger')
print(animals) # ['shark', 'tiger', 'elephant', 'snake']
# remove(value) will only remove the 1st matched item, and ignore all the following matched items.

# ValueError: list.remove(x): x not in list
# animals.remove('leopard')

# So you need to check whether the list contains the value or not
if 'leopard' in animals:
    animals.remove('leopard')
else:
    print("'leopard' doesn't exist in list animals")

# Similarly, you can use 'not in'
if 'penguine' not in animals:
    animals.append('penguine')
    print('penguine has been appended to animals')
    print(animals) # ['shark', 'tiger', 'elephant', 'snake', 'penguine']

# IMPORTANCE!!! ----------------------------------------------------
# 'in' operator tells you whether the item exists in the list or not
# ------------------------------------------------------------------
