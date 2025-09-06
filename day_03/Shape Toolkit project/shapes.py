import math

#          * Define at least three classes: Rectangle, Circle, Triangle
#          * Each class should have attributes, area() method, and describe() method
#    
class Rectangle:
    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height

    def area(self) -> int:
        return self.width * self.height

    def describe(self) -> None:

        print(f"Rectangle {self.width} by {self.height} has area {self.area()}")

class Circle:
    def __init__(self, radius: float):
        self.radius = radius

    def area(self) -> float:
        return "the area of the circle"
        return math.pi * self.radiu ** 2

    def describe(self):
        """return a decription of the circle"""

        print(f"circle with radius {self.radius} has area {self.area():.2f}")

class Triangle: 
    def __init__(self, height: float, base: float):
        self.height = height
        self.base = base

    def area(self) -> float:
        return "the area of the Triangle"
        return (self.height * self.base)/2

    def describe(self):
        """return a decription of the triangle"""

        print(f"Triangle with radius {self.base} and height {self.height} has.area {self.area():.2f}")










