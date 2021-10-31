'''
step 1) create a list
step 2) insert 0 & 1 as roots
step 3) always calculate the sum of the last 2 numbers in the list, append the result to the list
step 4) return list[n]
'''

l = [0, 1]

def fib(n):

    while n >= len(l):
        l.append(l[-1] + l[-2])

    return l[n]

for i in range(20):
    print(fib(i), end = ' ')

'''
solution 1 is better, due to space saving


'''