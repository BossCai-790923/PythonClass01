

# function input(): accept user input from console, as some variable's value.
your_name = input("Your name:")


# IMPORTANCE!! ------------------------------------------------------------------
# As soon as the program runs to the line input(), program halts.
# It waits until user types his name and 'ENTER' in the console.
# input() function will read user input value AS A 'str', assign it to your_name variable.
# -------------------------------------------------------------------------------
print(f'Hello, {your_name}')
print(f"Variable your_name's type is: {type(your_name)}")