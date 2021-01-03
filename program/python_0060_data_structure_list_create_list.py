'''
What is data structure?

Variable is like a pointer, points to a box which holds ONLY ONE value - int / float / boolean / str
Data Structure is like a cabinet, which contains many boxes!
When the variable pointer, points to a cabinet, then you can use the variable to open the cabinet, and use any value inside it'

The 1st data structure we learn today is called - list
'''


# Usage 1) Create list -------------------------------

# Solution 1) Use square bracket
fruits = ['Apple', 'Orange', 'Banana', 'Pear']
print(fruits)

animals = ['tiger',    # I can put 1 element per line
           'elephant',
           'snake',
           'shark']

print(animals)

cars = [] # Create an empty list
print(cars)


# Solution 2) Use list constructor
students = list() # Create an empty list
print(students)

numbers = list(range(10)) # pass in a range value to create a numbers list
print(numbers)

char_list = list("I love Python!") # pass in a str value to create char list
print(char_list)