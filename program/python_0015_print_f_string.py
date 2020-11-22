#Requirement: Print out str 'My Name is Bond, James Bond' using variable first_name and last_name

first_name = 'James'
last_name = 'Bond'

#[Solution 1] pass 4 str values to print() function
#[Problem] there is an extra space between Bond and ','
print('My name is', last_name, ',', first_name, last_name) #My name is Bond , James Bond

#[Solution 2] Use '+' to join 6 str values together, pass the newly-joined str value to print() function
#[Problem] Very messy, not readable.
print('My name is ' + last_name + ', ' + first_name + ' ' + last_name) #My name is Bond, James Bond

#[Solution 3] Python f string
# IMPORTANCE!! ------------------------------------------------------------------
# 1) Have an f at the beginning
# 2) Curly braces containing variables or expressions that will be replaced with their values
# -------------------------------------------------------------------------------
print(f'My name is {last_name}, {first_name} {last_name}') #My name is Bond, James Bond

#More examples
print(f'No, Mr {last_name}, I expect you to die!') # No, Mr Bond, I expect you to die!

age = 90
print(f'Sean Connery is now {age} years old.') # Sean Connery is now 90 years old.

language = 'Python'
rank = 1
who = 'all students'
kids_age = 15
teacher_surname = 'Fan'

print(f'{language} is the world no {rank} programming language, {who} should start learning it from age {kids_age} years old.')
print(f'And they all learn {language} with Teacher {teacher_surname}.')
print(f'{who} enjoy learning {language}, as {language} is quite fun, and Teacher {teacher_surname} is quite fun.')