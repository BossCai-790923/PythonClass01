'''
Requirement:
Output the mutiplication table as below
'''

'''
Logic is always the most important! When logic is clear, then we convert the logic to code.

Logic:

1) I can see there are in total 9 lines -> I loop for i in range(1, 10):

2) In each line, there are very similar items.
   In 1st row, there is 1 item. 
   In 2nd row, there are 2 items. 
   In 3rd row, there are 3 items.
   ...
   In 9th row, there are 9 items. 
   -> 
   for each row, I loop in range(1, i+1):
   
3) In each row, all those items are in same line -> I should use parameter end=' ' in the print statement, like what we've learnt in 0049   
'''

for row in range(1, 10):
    for item_index in range(1, row + 1):
        print(f'{item_index} * {row} = {item_index * row}', end=' ')
    print('')
