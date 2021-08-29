from turtle import *

colors = ['red', 'purple', 'blue', 'green', 'orange', 'yellow']


bgcolor('black')

for x in range(360):
    pencolor(colors[x % 6])
    width(x / 100 + 1)
    forward(x)
    left(59)
