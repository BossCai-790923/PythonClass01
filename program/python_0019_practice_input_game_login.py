#Requirement: Mimic online game user login

# define a multi-line str variable as the welcome message
welcome_msg = '''
**********************************
    Welcome to King of Glory
**********************************
'''

print(welcome_msg)


user_name = input("User Name:")
password = input("Password:")

print(f"Welcome, {user_name}! You've successfully logged in the game.")

total_coins = 0

short_of_coins_msg = f'Unfortunately, you have only {total_coins} coins in your account. Please top up your account.'
print(short_of_coins_msg)

coins_topup = int(input("Total coins to top up: ")) # convert str to int

# These 2 lines are the same
# total_coins = total_coins + coins_topup
total_coins += coins_topup

coins_requirement = 300

if total_coins < coins_requirement:
    print(f"You still do not have enough coins, you need to top up extra {coins_requirement - total_coins} coins")
else:
    print(f'Now you have coins: {total_coins}. You can continue to play the game.')