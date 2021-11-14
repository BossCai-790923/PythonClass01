

import numpy as np

'''
What is array?
Array is very similar to list, or it is almost a list

Difference:
1) array is fixed size
   list is not fixed size
   
2) array is homogenous (array can only put 1 TYPE of value)
   list is hetergenous (mixed TYPE)
   
3) array is much faster than list   
'''

print('1 dimension example 1 -------------------------------------')

a = np.array([1,2,3])
print(a)

a[1] = 4
print(a[0], a[-2], a[-1])


print('1 dimension example 2 -------------------------------------')

b = np.array([i for i in range(20)])
print(b)

c = b[::-1]
print(c)

d = b[2:16:2]
print(d)


print('2 dimension-----------------------------------------------')
e = np.array([ [3, 5, 2, 4],
           [7, 6, 8, 8],
           [1, 6, 7, 7]])

print(e)

'''
because e has 3 rows * 4 columns, so we say:
e's shape is 3 * 4
e is a 3 * 4 matrix
'''

print(e.shape)

print(e.T)
print(e.T.shape)

'''
e.T: e's transpose matrix -> 转置矩阵
'''


