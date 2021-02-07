'''
Assume L is a list, expression L[start:stop:step] returns a portion of list L starts from index start(inclusive) to index stop(exclusive), at a step size step.

Slice syntax:
                L[start:stop:step]

start: start position
stop: stop position
step: the increment
'''

L = list('abcdefghi')
print(L)

# positive index:     0    1    2    3    4    5    6    7    8
#                   ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']
# negative index:    -9   -8   -7   -6   -5   -4   -3   -2   -1

print("1) Basic Example ---------------------------------")
# L[2] in included. L[7] is excluded.
# This is the same as range(2,10), which generates number [2,10), 2 is included (closed interval), 10 is excluded (open interval)
print(L[2:7]) # Please figure out & type the output value here, run it, verify your answer.
# start: 2
# stop: 7
# step: 1
# L[2:7] doesn't have step, so Python assumes step equals to 1
# so L[2:7] equals to L[2:7:1]
print(L[2:7:1]) # Please figure out & type the output here, run it, verify your answer.


print("2) Slice with Negative Indices ------------------")
print(L[-7:-2]) # Please figure out & type the output here, run it, verify your answer.
# start: -7
# stop: -2
# step: 1
# L[-7:-2] doesn't have step, so Python assumes step equals to 1
# so L[-7:-2] equals to L[-7:-2：1]
print(L[-7:-2:1]) # Please figure out & type the output here, run it, verify your answer.


print("3) Slice with Positive & Negative Indices ------------------")
print(L[2:-5]) # Please figure out & type the output here, run it, verify your answer.

print("4) Specify Step of the Slicing ------------------------------")
print(L[2:7:2]) # Please figure out & type the output here, run it, verify your answer.

print("5) Negative Step Size ---------------------------------------")
print(L[6:1:-2]) # Please figure out & type the output here, run it, verify your answer.

print("6) Slice at Beginning & End ---------------------------------")
print(L[:3]) # Please figure out & type the output here, run it, verify your answer.
#L[:3] doesn't have step, so Python assumes step equals to 1
# When step equals to 1, when start is missing, Python assumes slice start from the left beginning.
#L[:3] equals to L[0:3]

print(L[6:]) # Please figure out & type the output here, run it, verify your answer.
#L[6:] doesn't have step, so Python assumes step equals to 1
# When step equals to 1, when stop is missing, Python assumes slice end till the right end.
#L[6:] equals to L[6:len(L)]

print("7) Reverse a list ---------------------------------")
print(L[::-1]) # Please figure out & type the output here, run it, verify your answer.
# start is missing, stop is missing, step = -1
# In this case, Python assumes start equals to the right end, stop equals to the left beginning.

print("8) Modify Multiple list values ------------------------")
L = list("abcde")

# positive index:     0    1    2    3    4
#                   ['a', 'b', 'c', 'd', 'e']
# negative index:    -5   -4   -3   -2   -1
L[1:4] = [1,2,3]
print(L) # Please figure out & type the output here, run it, verify your answer.

L = list("abcde")
L[1:2] = [1,2,3]
print(L) # Please figure out & type the output here, run it, verify your answer.

print("9) Insert Multiple List Items ------------------------")
L = list("abc")

# positive index:     0    1    2
#                   ['a', 'b', 'c',]
# negative index:    -3   -2   -1

L[:0] = [1,2,3]
# L[:0] doesn't have step, so step = 1
# When step = 1, start is missing, Python assumes slice start from the left beginning.
# L[:0] equals to L[0:0]
# When start equals to stop, it points to a POSITION on the left of the index
print(L) # Please figure out & type the output here, run it, verify your answer.

L = list("abc")
L[len(L):] = [1,2,3]
#L[len(L):] doesn't have step, so step = 1
#When step = 1, stop is missing, Python assumes slice end till the right end.
#L[len(L):] equals ot L[len(L):len(L)]
# When start equals to stop, it points to a position on the left of the index.
# So L[len(L):len(L)] points to the right of 'c'
print(L) # Please figure out & type the output here, run it, verify your answer.


print("10) Delete Multiple List Items ------------------------")
L = list("abcde")


# positive index:     0    1    2    3    4
#                   ['a', 'b', 'c', 'd', 'e']
# negative index:    -5   -4   -3   -2   -1

L[1:5] = []
print(L)

L = list("abcde")
del L[1:5]
print(L)

print("11) Clone or Copy a list ----------------------------")
L = list("abcde")
print(L)

L2 = L[:]
print(L2)
print(L2 is L) # False
# 'is' operator is to check whether they are the same object, or they are different objects with same value.