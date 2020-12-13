'''
Inside the while loop body:

Step1) So we still use top-down coding solution, finish the skeleton first:

    if user_a_choice = 'scissors':
        pass # place holder
    elif user_a_choice = 'paper':
        pass
    elif user_a_choice = 'stone':
        pass
    else:
        wrong input

Step 2) in the 3 passes above, fill in this part:

    if user_b_choice = 'scissors':
        pass # place holder
    elif user_b_choice = 'paper':
        pass
    elif user_b_choice = 'stone':
        pass
    else:
        wrong input

Step 3) fill in the flesh

'''

user_a_choice = input("User A's choice(scissors / paper / stone / exit): ")

while user_a_choice != 'exit':

    user_b_choice = input("User B's choice(scissors / paper / stone): ")

    if user_a_choice == 'scissors':
        if user_b_choice == 'scissors':
            print(f"User A {user_a_choice}, User B {user_b_choice}: Draw.")
        elif user_b_choice == 'paper':
            print(f"User A {user_a_choice}, User B {user_b_choice}: User A Wins.")
        elif user_b_choice == 'stone':
            print(f"User A {user_a_choice}, User B {user_b_choice}: User B Wins.")
        else:
            print(f"User B inputs a wrong choice: {user_b_choice}")
    elif user_a_choice == 'paper':
        if user_b_choice == 'scissors':
            print(f"User A {user_a_choice}, User B {user_b_choice}: User B Wins.")
        elif user_b_choice == 'paper':
            print(f"User A {user_a_choice}, User B {user_b_choice}: Draw.")
        elif user_b_choice == 'stone':
            print(f"User A {user_a_choice}, User B {user_b_choice}: User A Wins.")
        else:
            print(f"User B inputs a wrong choice: {user_b_choice}")
    elif user_a_choice == 'stone':
        if user_b_choice == 'scissors':
            print(f"User A {user_a_choice}, User B {user_b_choice}: User A Wins.")
        elif user_b_choice == 'paper':
            print(f"User A {user_a_choice}, User B {user_b_choice}: User B Wins.")
        elif user_b_choice == 'stone':
            print(f"User A {user_a_choice}, User B {user_b_choice}: Draw.")
        else:
            print(f"User B inputs a wrong choice: {user_b_choice}")
    else:
        print(f"User A inputs a wrong choice: {user_a_choice}")

    # IMPORTANT !!! ----------------------------------------------------
    # Update looping condition
    # ------------------------------------------------------------------
    user_a_choice = input("User A's choice(scissors / paper / stone / exit): ")
