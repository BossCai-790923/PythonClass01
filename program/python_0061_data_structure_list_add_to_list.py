fruits = ['Apple', 'Orange', 'Banana', 'Pear']
animals = ['tiger', 'elephant', 'snake', 'shark']

# Solution 1: User append - add new value to the END of the list
fruits.append('Watermelon')
print(fruits)

# List can be heterogeneous (Contains all kinds of objects)
fruits.append(True) # add boolean to the end of the list
fruits.append(1) # add int to the end of the list
fruits.append(1.2) # add float to the end of the list
fruits.append([1, 2, 3]) # add another list
print(fruits) # ['Apple', 'Orange', 'Banana', 'Pear', 'Watermelon', True, 1, 1.2, [1, 2, 3]]

'''
       ['tiger', 'elephant', 'snake', 'shark']
index     0           1         2        3   
          -4         -3         -2      -1
'''


# Solution 2: Use insert - add new value to the list at index specified
animals.insert(1, 'leopard')
print(animals) # ['tiger', 'leopard', 'elephant', 'snake', 'shark']

animals.insert(100, 'giraffe') # when index > length of the list, insert it to the END of the list
print(animals) # ['tiger', 'leopard', 'elephant', 'snake', 'shark', 'giraffe']

animals.insert(-2, 'hedgehog') # ['tiger', 'leopard', 'elephant', 'snake', 'hedgehog', 'shark', 'giraffe']
print(animals)


# Solution 3: Use extend - join another list
insects = ['catepillar', 'ant', 'butterfly']
animals.extend(insects)
print(animals) # ['tiger', 'leopard', 'elephant', 'snake', 'hedgehog', 'shark', 'giraffe', 'catepillar', 'ant', 'butterfly']

# animals.append(insects) # ['tiger', 'leopard', 'elephant', 'snake', 'hedgehog', 'shark', 'giraffe', ['catepillar', 'ant', 'butterfly']]
# print(animals)




# Solution 4: Use + to join another list
birds = ['swallow', 'eagle', 'toucan']
animals = animals + birds
# animals += birds
print(animals) # ['tiger', 'leopard', 'elephant', 'snake', 'hedgehog', 'shark', 'giraffe', 'catepillar', 'ant', 'butterfly', 'swallow', 'eagle', 'toucan']



# Solution 5: Use * to duplicate list
many_birds = birds * 3
print(many_birds) # ['swallow', 'eagle', 'toucan', 'swallow', 'eagle', 'toucan', 'swallow', 'eagle', 'toucan']

zero_list = [0] * 100
print(zero_list)