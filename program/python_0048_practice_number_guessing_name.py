'''
Requirement:

Build a Number guessing game, in which the user selects a range, for example: 1, 100.
And your program will generate some random number in the range, for example: 42.
And the user needs to guess the number.
If his answer is 50, then you need to tell him. “Try Again! You guessed too high”
If his answer is 20, then you need to tell him. “Try Again! You guessed too low”
When he finally guesses it, you need to tell him, how many times he guesses.
'''

'''
Solution:
Step 1) Get lower bound / upper bound from console
Step 2) Use random module to generate a number in the range as the answer
Step 3) Loop to ask the user "what's the correct answer?", and tell him/her higher or lower. If it is correct, exit. 
'''




import random

# Step 1) Get lower bound / upper bound from console
lower = int(input("Enter positive lower bound: "))
upper = int(input("Enter positive upper bound: "))

# Step 2) Use random module to generate a number in the range as the answer
answer = random.randint(lower, upper)

count = 0

# Step 3) Loop to ask the user "what's the correct answer?", and tell him/her higher or lower. If it is correct, exit.
while True:

    # Step 3.1) Get user guess
    guess_result = int(input("Guess a number: "))

    # Step 3.2) update the count
    count += 1

    # Step 3.3) check user guess
    if answer == guess_result:
        print(f"Congrats! You did it {count} try.")
        break

    elif answer > guess_result:
        print("Try again! You guessed too low.")

    else:
        print("Try again! You guessed too high.")