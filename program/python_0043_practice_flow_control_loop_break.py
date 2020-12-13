# Requirement:
# Continuously get user input from console, ask user to input a number
# If the number is divisible by 7, then tell the user 'The number is divisible by 7! Program exit!!"
# Otherwise, ask user try again.

while True:
    input_number = int(input("Please input a number: "))
    if input_number % 7 == 0:
        print(f"{input_number} is divisible by 7! Program exits.")
        break
    else:
        print(f"{input_number} is NOT divisible by 7! Please try again.")

