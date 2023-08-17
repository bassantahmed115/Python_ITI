import math

class Shape:
    count = 0

    def __init__(self, name, color, dimensions):
        self.name = name
        self.color = color
        self.dimensions = dimensions
        Shape.count += 1

    def area(self):
        return self.dimensions[0] * self.dimensions[1]

    def __str__(self):
        return f"Name: {self.name}, Color: {self.color}, Dimensions: {self.dimensions[0]} x {self.dimensions[1]}, Area = {self.area()}"

class Circle(Shape):
    count = 0

    def __init__(self, rad, color):
        super().__init__("Circle", color, (2 * rad, 2 * rad))
        self.rad = rad
        Circle.count += 1

    def area(self):
        return math.pi * self.rad ** 2

# Creating objects
shape1 = Shape("Rectangle", "pink", (10, 6))
shape2 = Shape("Square", "orange", (5, 3))
circle1 = Circle(7, "yellow")

# Printing objects and counts
print(str(shape1))
print(f"Rectangle Area = {shape1.area()}")

print(f"Square Area = {shape2.area()}")
print(str(shape2))

print(f"Circle Area = {circle1.area()}")

print(f"Number of shapes created: {Shape.count}")

print(f"Number of circles created: {Circle.count}")
