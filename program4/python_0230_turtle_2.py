from turtle import *

def square(length):
    for i in range(4):
        forward(length)
        right(90)

for i in range(365 // 5):
    square(100)
    right(5)

done()