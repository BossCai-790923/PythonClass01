from math import sqrt

# CLASS DEFINITION BEGIN ==========================

class Point:

    def __init__(self, x, y):
        pass

    def move_to(self, x, y):
        pass


    def move_by(self, dx, dy):
        pass

    def distance_to(self, other):
        pass

    def __str__(self):
        pass

    def to_tuple(self):
        '''
        Create a tuple from x and y
        '''
        pass


# MAIN PROGRAM BEGIN =================================

if __name__ == '__main__':

    print("Creating p1 -------------------------")
    p1 = Point(-10, -10)

    print("Moving p1 to -------------------------")
    p1.move_to(3, 5)

    print("p1 location -------------------------")
    print(f"p1 location: {p1}")

    print("Creating p2 -------------------------")
    p2 = Point(0, 0)

    print("Moving p2 by-------------------------")
    p2.move_by(-1, 2)

    print("p2 location -------------------------")
    print(f"p2 location: {p2}")

    print("Calculating p1 to p2 distance -------")
    print(p1.distance_to(p2))