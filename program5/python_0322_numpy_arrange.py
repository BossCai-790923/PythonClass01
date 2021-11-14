
import numpy as np

print('1 dimensional array ----------')

# means array range
a = np.arange(10)
print(a)

print(a.shape)

print('2 dimensional array ----------')
c = np.arange(20).reshape(5, 4)
print(c)
print(c.T)

print(c[3])
print(c[3][2])

print('3 dimensional array ----------')

d = np.arange(60).reshape(3,4,5)
print(d)
print(d.shape)

print(d[2][2])
print(d[2][2][2])