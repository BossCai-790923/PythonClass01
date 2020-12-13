choice_a = "a"
choice_b = "b"
while not choice_a.lower() == "exit":
    choice_a = input("Choose Scissors, Paper, Stone, or Exit: ")
    if choice_a.lower() == "exit":
        exit()
    elif not choice_a.lower() == "scissors" and not choice_a.lower() == "paper" and not choice_a.lower() == "stone":
        print("Please enter a valid selection.")
        continue
    choice_b = input("Choose Scissors, Paper or Stone: ")
    if not choice_b.lower() == "scissors" and not choice_b.lower() == "paper" and not choice_b.lower() == "stone":
        print("Please enter a valid selection.")
        continue
    if choice_a.lower() == "scissors":
        compare_a = 3
    elif choice_a.lower() == "paper":
        compare_a = 2
    elif choice_a.lower() == "stone":
        if choice_b.lower() == "scissors":
            print("Player a wins!")
            continue
        elif choice_b.lower() == "paper":
            print("Player b wins!")
            continue
        else:
            compare_a = 1

    if choice_b.lower() == "scissors":
        compare_b = 3
    elif choice_b.lower() == "paper":
        compare_b = 2
    elif choice_b.lower() == "stone":
        if choice_a.lower() == "scissors":
            print("Player b wins!")
            continue

        elif choice_a.lower() == "paper":
            print("Player a wins!")
            continue

        else:
            compare_b = 1

    if compare_a > compare_b:
        print("Player a wins!")
    elif compare_a < compare_b:
        print("Player b wins!")
    else:
        print("It's a tie!")
