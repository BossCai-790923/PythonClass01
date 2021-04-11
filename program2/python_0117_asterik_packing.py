def calculate_sum(*list):
    print(type(list)) # Tuple
    return sum(list)

result1 = calculate_sum(1, 2, 3, 4, 5) #Passing in 5 arguments to function calculate_sum
print(result1)

'''
Explanation:
Code execution flows from 'function caller' to 'function body'

function caller     ->      function body
1,2,3,4,5                   *list

When asterisk (*) appears in 'function body parameter' position,
This equals to convert multiple values to a tuple

This is called: asterisk packing
'''