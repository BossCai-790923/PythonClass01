'''
Requirement:
A frog can jump up to one step at a time or up to two steps.
How many jumping solutions are there for the frog to jump up n steps?

1 -> 1
2 -> 2
3 -> 3

'''


'''
Question 1)
Original question: How many jumping solutions are there for the frog to jump up n steps?

f(n)
param n  means steps count
f(n)     means solutions count


Question 2) What's the base case?
When n = 1, return 1
When n = 2, return 2


Question 3) What's the state transition? From THE problem to same-nature subproblem.  
Because the frog always jumps 1 step or 2 steps, so
the total jump solution count for 100 steps -> f(100)
equals to the sum of
the total jump solution count for 99 steps -> f(99)
the total jump solution count for 98 steps -> f(98)

f(n) = f(n-1) + f(n-2)
'''

# naive recursive
def f0(n): # n means steps count

    # base case
    if n <= 2:
        return n

    # recursive call
    return f0(n-2) + f0(n-1)

for i in range(1, 21):
    print(f"for steps count: {i}, there are {f0(i)} jump solutions")

print("--------------------------------------------")

dp = [0 for _ in range(51)]
dp[1] = 1
dp[2] = 2

'''
IMPORTANCE !!! ----------------------------------------------
1) index of dp array -> index means steps count
2) value of dp array -> value means total solutions count

dp[1] is 1, means there are total 1 solution for the frog to jump 1 step
dp[2] is 2, means there are total 2 solution for the frog to jump 2 steps
-------------------------------------------------------------
'''

# dp top down
def f1(n): # another naming -> memorized dp

    # base case
    if n <= 2:
        return n

    if dp[n] != 0:
        return dp[n]

    dp[n] = f1(n-2) + f1(n-1)
    return dp[n]

for i in range(1, 51):
    print(f"for steps count: {i}, there are {f1(i)} jump solutions")

print("--------------------------------------------")


dp = [0 for _ in range(51)]
dp[1] = 1
dp[2] = 2

# dp bottom up
def f2(n): # another name -> tabulated dp

    if dp[n] != 0:
        return dp[n]

    for i in range(3, n+1):
        if dp[i] == 0:
            dp[i] = dp[i-2] + dp[i-1]

    return dp[n]


for i in range(1, 51):
    print(f"for steps count: {i}, there are {f2(i)} jump solutions")

