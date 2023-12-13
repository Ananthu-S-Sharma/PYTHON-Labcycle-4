class Rectangle:
    def __init__(self):
        self._length = int(input("Enter the length: "))
        self._breadth = int(input("Enter the breadth: "))
        self._area = self._length * self._breadth

    def greaterThan(self, other_rectangle):
        if self._area < other_rectangle._area:
            print("Area of Rectangle 1 is Greater")
        else:
            print("Area of Rectangle 2 is Greater")

print("Rectangle 1:")
r1 = Rectangle()
print("Rectangle 2:")
r2 = Rectangle()
print("Comparing Rectangles:")
r2.greaterThan(r1)
