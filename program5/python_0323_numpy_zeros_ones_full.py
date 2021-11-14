import numpy as np

print("np.ones -----------------------")
a = np.ones([4])
print(a)


print("np.zeros -----------------------")
# int8, int16, int32, int64
b = np.zeros([2,3], dtype=np.int32)
print(b)

b[1,2] += 5
print(b)

print("np.full ------------------------")
c = np.full([3,5,2], -1, dtype=np.int32)
print(c)
