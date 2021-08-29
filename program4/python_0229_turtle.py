from turtle import *

# -square ---------------------------

pencolor('green')
for i in range(4):
    forward(50) # draw straight line 50 unit
    right(90) # turn right 90 degree

# -star -------------------------------
penup()
goto(100, 100)
pendown()

pencolor('red')
for i in range(5):
    forward(100)
    right(144)

# -circle 1 ---------------------------
penup()
goto(-100, 100)
pendown()

pencolor('blue')
for i in range(360 // 10): # 10 degree * 36 = 360 degree
    forward(10)
    right(10)



# -circle 2 -------------------------
penup()
goto(0, 100)
pendown()

pencolor('yellow')
circle(100)


# -flower ----------------------------
penup()
goto(-100, -100)
pendown()

pencolor('pink')
for i in range(100):
    forward(100)
    left(123)


done()
