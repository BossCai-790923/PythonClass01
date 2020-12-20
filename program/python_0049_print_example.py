

# By default, print() inserts a space between the items it prints.
# You can change this by using the sep parameter.
print(1,2,3)
print(1,2,3, sep='-')
print(1,2,3, sep=' * ')
print(1,2,3, sep='\n') # this is next line

print("------------------------------------------------")

# By default, print() add a \n at the end of what it prints.
# You can change this by using the end parameter.

for i in range(5):
    print(i)

print("------------------------------------------------")

for i in range(5):
    print(i, end=' ')
