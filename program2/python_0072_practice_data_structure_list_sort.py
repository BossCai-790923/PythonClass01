'''
Requirement:
1) Ask user to input number from console
2) Add the number to the list in the correct order, so that the numbers are sorted asscendingly
3) Print list to the console
4) Exit the program when user input 'exit'
'''


# Step 0) I define a list variable my_list, this is to hold all numbers from user.
my_list = []

# Step 1) this is to store number input from console from user
new_number_str = input("Next number:")


# Step 2) I loop until new_number_str is 'exit'
while 'exit' != new_number_str:

    # Step 2.1) I convert the str new_number_str to int variable new_number
    new_number = int(new_number_str)

    # Step 2.2) I need to find the correct place where I should insert the new_number into my_list
    # Initially, I set new_number_index to 0, which means I insert new_number at index 0 of my_list
    new_number_index = 0

    # Step 2.3) I loop my_list
    #           I increase new_number_index as long as number is smaller than new_number, which means I need to loop
    #           until I find a number bigger than new_number, that's where I should insert new_number into my_list
    for number in my_list:
        if number < new_number:
            new_number_index += 1
        else:
            break

    # Step 2.4) Insert new_number to my_list at place - new_number_index
    my_list.insert(new_number_index, new_number)
    print(my_list)


    # Step 2.5) Update loop condition: Read next number from user
    new_number_str = input("Next number:")

