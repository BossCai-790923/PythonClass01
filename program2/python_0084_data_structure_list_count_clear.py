fruits = ['Apple', 'Orange', 'Banana', 'Pear'] * 2

fruits.remove('Orange')
fruits.append('Apple')

print(fruits) # ['Apple', 'Banana', 'Pear', 'Apple', 'Orange', 'Banana', 'Pear', 'Apple']


# -fruits.count('Orange') ----------------------------------------

print(f"There are {fruits.count('Orange')} 'Orange' in fruits.")
print(f"There are {fruits.count('Apple')} 'Apple' in fruits.")
print(f"There are {fruits.count('Banana')} 'Banana' in fruits.")

# -fruits.clear() -------------------------------------------------
fruits.clear()
print(fruits)