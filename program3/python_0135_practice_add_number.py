'''
find the value of s
s = a + aa + aaa + aaaa + aa...a，
a can be any number from 1 to 9
term count comes from user input in console.

For example:
Enter the base number: 2
Enter the term count: 5
The answer is 24690

Explanation:
2 + 22 + 222 + 2222 + 22222 is 24690
'''

#Observation
# term 0 - 5
# term 1 - 55 = 5 * 10 + 5
# term 2 - 555 = 5 * (5 * 10 + 5) + 5
# term 3 - 5555 = 5 * (5 * (5 * 10 + 5) + 5) + 5

#Summary
# term 0 = Loop 0 times [* 10 + 5]
# term 1 = Loop 1 times [* 10 + 5]
# term 2 = Loop 2 times [* 10 + 5]
# term 3 = Loop 3 times [* 10 + 5]

def solution1_math1(base_number, term_count):
    sum = 0

    for term_no in range(term_count):
        term_value = base_number

        for _ in range(term_no):
            term_value = term_value * 10 + base_number

        sum += term_value

    return sum

'''
Question:
How many times the calculate (line 35) will be executed?
Let's say, in total we have n terms.
Answer: 1 + 2 + 3 ... + n
      = (1 + n) * n / 2
      = 1/2 * n^2 + 1/2 * n
      
Time Complexity: O(n^2)
-----------------------------------------------------------------------------------
Time Complexity means: how code slows as data grows
Time Complexity answer this question: how much slower the code will go if you give it ten times more data.
We use Big-O to express this.

When n = 10;  it calculate = 1/2 * 10 * 10     + 1/2 * 10   = 50    + 5  = 55   times      
When n = 100; it calculate = 1/2 * 100 * 100   + 1/2 * 100  = 5000  + 50 = 5050 times - when data grows 10 times, roughly, code slows 100 times.      
The driven factor is n^2, (1/2 * n) can be ignored.
So we say: Big-O(n^2)

O(1)
O(n)
O(n^2)


'''

# Solution 1 can be optimized

# term 0 - 5
# term 1 - 55 = (term 0 * 10) + 5
# term 2 - 555 = (term 1 * 10) + 5

def solution2_math1_optimized(base_number, term_count):
    sum = 0

    term_value = base_number    # put term 0 into sum
    sum += term_value

    for _ in range(term_count - 1):                         # repeat term_count - 1 times, since we start from term 1
        term_value = term_value * 10 + base_number          # calculate the next value of 'term_value'
        sum += term_value                                   # add to sum

    return sum



def solution3_math2(base_number, term_count):
    sum = 0

    for x in range(term_count):

        '''
        1 = 10^0
        11 = 10 + 1 = 10^1 + 10^0
        111 = 100 + 10 + 1 = 10^2 + 10^1 + 10^0
        '''
        for j in range(x+1):
            sum += 10 ** j

    return sum * base_number


def solution4_math2_optimized(base_number, term_count):
    term_value = 0
    sum = 0
    for i in range(term_count):
        term_value = term_value + (10 ** i) * base_number
        sum += term_value

    return sum


def solution5_math3(base_number, term_count):
    '''
    The idea is to calculate the sum directly from those numbers
    '''
    sum = 0
    for term_index in range(1, term_count + 1):
        sum += 10 ** (term_index - 1) * (term_count + 1 - term_index) * base_number

    return sum


def solution6_str_manipulation(base_number, term_count):
    sum = 0
    for x in range(1, term_count + 1):
        sum += int(str(base_number) * x)
    return sum


def solution7_eval(base_number, term_count):
    '''
    The idea is to build the expression directly.
    And I use built-in function eval(expression) to calculate the result directly
    '''
    expression = ''
    for i in range(1, term_count + 1):
        expression += str(base_number) * i
        if i < term_count:
            expression += '+'

    print("Here comes the expression: ", expression)
    sum = eval(expression)
    return sum

# -main program -------------------------------------
base_number = int(input("Enter the base number: "))
term_count = int(input("Enter the term count: "))

result = solution1_math1(base_number, term_count)
print("The answer is: ", result)

result = solution2_math1_optimized(base_number, term_count)
print("The answer is: ", result)

result = solution3_math2(base_number, term_count)
print("The answer is: ", result)

result = solution4_math2_optimized(base_number, term_count)
print("The answer is: ", result)

result = solution5_math3(base_number, term_count)
print("The answer is: ", result)

result = solution6_str_manipulation(base_number, term_count)
print("The answer is: ", result)

result = solution7_eval(base_number, term_count)
print("The answer is: ", result)