user_a = input("User_a: scissors / paper / stone / exit  ")
while user_a != 'exit':
    user_b = input("User_b: scissors / paper / stone  ")
    if user_a == "scissors":
        if user_b == "paper":
            print("user_a wins")
        elif user_b == "stone":
            print("user_b wins")
        elif user_b == "scissors":
            print("It is a draw")
        else:
            print("Unrecognised. Please insert again")
    elif user_a == "paper":
        if user_b == "stone":
            print("user_a wins")
        elif user_b == "scissors":
            print("user_b wins")
        elif user_b == "paper":
            print("It is a draw")
        else:
            print("Unrecognised. Please insert again")
    elif user_a == "stone":
        if user_b == "scissors":
            print("user_a wins")
        elif user_b == "paper":
            print("user_b wins")
        elif user_b == "stone":
            print("It is a draw")
        else:
            print("Unrecognised. Please insert again")
    else:
        print("Unrecognised. Please insert again")
    user_a = input("User_a: scissors / paper / stone / exit  ")
