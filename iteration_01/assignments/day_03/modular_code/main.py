from shapes import Rectangle, Circle, Triangle
from utils import cm2_to_m2, compare_areas

choice = input("Choose a shape (rectangle, circle, triangle): ")

if choice == "rectangle":
    w = float(input("Enter width: "))
    h = float(input("Enter height: "))
    shape = Rectangle(w, h)
elif choice == "circle":
    r = float(input("Enter radius: "))
    shape = Circle(r)
elif choice == "triangle":
    b = float(input("Enter base: "))
    h = float(input("Enter height: "))
    shape = Triangle(b, h)
else:
    print("Invalid choice.")
    shape = None

if shape:
    shape.describe()
    print("Area in m^2:", cm2_to_m2(shape.area()))
    compare_areas(shape, Rectangle(10, 10))
