'''
Task 1)
Read this article: https://www.mathscareers.org.uk/calculating-pi/

Task 2)
Use the following 2 solutions to calculate pi:
1) Gregory-Leibniz Series
2) Nilakantha Series

Task 3)
See how many correct digits you can get using either one of them.
You can compare your pi value with the actual pi value at website:
http://www.geom.uiuc.edu/~huberty/math5337/groupe/digits.html
'''

import math

def solution1_math_pi():
    print("Solution 1) Using math.pi")
    print(math.pi)
    print("-" * 50)

'''
Summary:
Actual pi: 3.141592653589793 238462643383279502884197169399375105820974944592307816406286
it prints: 3.141592653589793
We get 15 accurate digits.
'''


#Solution 2 --------------------------
# Ggregory-Leibniz Series
# pi / 4 = 1 - 1/3 + 1/5 - 1/7 ....

def solution2_leibniz():
    print("Solution 2) Using Gregory-Leibniz Series")
    # Step 1) define a variable
    quarter_of_pi = 0

    # Step 2) I loop and calculate quarter_of_pi
    # index = 1  ->  entry = 1/1 - 1/3       -> 1/index - 1/(index + 2)
    # index = 5  ->  entry = 1/5 - 1/7       -> 1/index - 1/(index + 2)
    # index = 9  ->  entry = 1/9 - 1/11      -> 1/index - 1/(index + 2)

    for index in range(1, 9000000, 4): # range works similar as slice ( start, stop, step)
        entry = (1/index) - (1/(index + 2))
        quarter_of_pi += entry

    value_of_pi = quarter_of_pi * 4
    print(f"{value_of_pi:.100f}")
    print("-" * 50)

'''
Summary:
Actual pi: 3.141592 653589793238462643383279502884197169399375105820974944592307816406286
it prints: 3.141592 43136777188709629626828245818614959716796875
We use 9,000,000 terms, we only get 6 accurate digits.

Conclusion: This is not an effective solution, or a bad algorithm. Because it converges slowly.  
'''

# Solution 3 -----------------------------
# pi = 3 + 4/(2*3*4) - 4/(4*5*6) + 4/(6*7*8) - 4/(8*9*10) .....

def solution3_nilakantha():
    print("Solution3) Using Nilakantha Series")
    value_of_pi = 3
    # Step 1) Summarize the relationship between my loop variable index and entry
    # index = 2   ->  entry = 4/(2*3*4) - 4/(4*5*6)         -> 4/(index * (index+1) * (index+2)) - 4/((index+2) * (index+3) * (index+4))
    # index = 6   ->  entry = 4/(6*7*8) - 4/(8*9*10)        -> 4/(index * (index+1) * (index+2)) - 4/((index+2) * (index+3) * (index+4))
    for index in range(2, 9000000, 4):
        denominator1 = index * (index + 1) * (index + 2)
        denominator2 = (index + 2) * (index + 3) * (index + 4)
        entry = 4 / denominator1 - 4 / denominator2
        value_of_pi += entry

    print(value_of_pi)

'''
Summary:
Actual pi: 3.141592653589 793238462643383279502884197169399375105820974944592307816406286
it prints: 3.141592653589 5253
We use 9,000,000 terms, we get 12 accurate digits. 
'''



# solution1_math_pi()
# solution2_leibniz()
solution3_nilakantha()

'''
https://en.wikipedia.org/wiki/Chronology_of_computation_of_%CF%80
'''