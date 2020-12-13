print(f'Input "exit" to exit.')
user_a = input(f'user_a, scissors,paper,or stone?: ')

while user_a != 'exit':
    user_b = input(f'user_b, scissors,paper or stone?: ')
    if user_a == 'exit':
        print(f'The game has ended.')
        print(f'New game:')
        user_a = input(f'user_a, scissors,paper,or stone?: ')
        user_b = input(f'user_b, scissors,paper or stone?: ')
    else:
        if user_a == 'exit' or user_b == 'exit':
            print(f'The game has ended.')
            print(f'New game:')
        elif user_a == 'scissors':
            if user_b == 'paper':
                print(f'user_a has won.')
            elif user_b == 'stone':
                print(f'user_b has won.')
            elif user_b == 'scissors':
                print(f'It is a draw.')
            else:
                print(f'There is a problem.')
        elif user_a == 'paper':
            if user_b == 'paper':
                print(f'It is a draw.')
            elif user_b == 'stone':
                print(f'user_a has won.')
            elif user_b == 'scissors':
                print(f'user_b has won.')
            else:
                print(f'There is a problem.')
        elif user_a == 'stone':
            if user_b == 'paper':
                print(f'user_b has won.')
            elif user_b == 'stone':
                print(f'It is a draw.')
            elif user_b == 'scissors':
                print(f'user_a has won.')
            else:
                print(f'There is a problem.')
        else:
            print(f'There is a problem.')
        user_a = input(f'user_a, scissors,paper,or stone?: ')
        user_b = input(f'user_b, scissors,paper or stone?: ')