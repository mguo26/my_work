import math

class Rectangle:
    """A rectangle defined by width and height."""
    def __init__(self, width, height):
        """Initialize a rectangle with width and height."""
        self.width = width
        self.height = height
    def area(self):
        """Return the area of the rectangle (width * height)."""
        return self.width * self.height
    def describe(self):
        """Print a description of the rectangle."""
        print(f"Rectangle {self.width} x {self.height} has area {self.area()}")

class Circle:
    """A circle defined by its radius."""
    def __init__(self, radius):
        """Initialize a circle with radius."""
        self.radius = radius
    def area(self):
        """Return the area of the circle (pi * r^2)."""
        return math.pi * self.radius ** 2
    def describe(self):
        """Print a description of the circle."""
        print(f"Circle with radius {self.radius} has area {self.area()}")

class Triangle:
    """A triangle defined by base and height."""
    def __init__(self, base, height):
        """Initialize a triangle with base and height."""
        self.base = base
        self.height = height
    def area(self):
        """Return the area of the triangle (0.5 * base * height)."""
        return 0.5 * self.base * self.height
    def describe(self):
        """Print a description of the triangle."""
        print(f"Triangle base {self.base}, height {self.height} has area {self.area()}")
