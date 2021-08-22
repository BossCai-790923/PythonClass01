from python_0227_practice_oop_basic_point import Point
import turtle


# CLASS DEFINITION BEGIN ==========================

class Line():
    def __init__(self, point_a, point_b, color):
        pass

    def length(self):
        pass

    def draw(self):
        pass

# PREPARE DATA BEGIN =================================

p1 = Point(30, 50)
p2 = Point(-10, 20)
p3 = Point(50, 20)
line1 = Line(p1, p2, 'green')
line2 = Line(p2, p3, 'red')
line3 = Line(p1, p3, 'yellow')



# MAIN PROGRAM BEGIN =================================

if __name__ == '__main__':
    print(f'line1 length: {line1.length()}')
    print(f'line2 length: {line2.length()}')
    print(f'line3 length: {line3.length()}')

    line1.draw()
    line2.draw()
    line3.draw()

    turtle.hideturtle()
    turtle.exitonclick()
