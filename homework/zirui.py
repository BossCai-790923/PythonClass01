from math import sqrt

# CLASS DEFINITION BEGIN ==========================


class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        print(f"New point ({x, y}) is created.")

    def move_to(self, x, y):
        self.bx = self.x
        self.by = self.y
        self.x = x
        self.y = y
        print(f"Moving point ({self.bx, self.by}) to ({x, y}).")

    def move_by(self, dx, dy):
        print(f"Moving point ({self.x, self.y}) by ({dx, dy}).")
        self.x += dx
        self.y += dy
        print(f"Current location: ({self.x, self.y})")

    def distance_to(self, other):
        print(sqrt((self.x-other.x)**2 + (self.y-other.y)**2))

    def to_tuple(self):
        return (self.x, self.y)

    def __str__(self):
        return f"({self.x}, {self.y})"


# MAIN PROGRAM BEGIN =================================

if __name__ == '__main__':

    print("Creating p1 -------------------------")
    p1 = Point(-10, -10)

    print("Moving p1 -------------------------")
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