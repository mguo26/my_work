
#          * Import classes from shapes.py
#          * Import helper functions from utils.py
#          * Allow user to create shapes (input dimensions)
#          * Print area and descriptions

from shapes import Rectangle, Circle, Triangle
import utils

print(utils.__file__)
def welcome_message() -> None:
    print("Welcome to the Shape Toolkit!")
    print("We support Rectangles, Circles, and Triangles.")
    print("Let's see some examples...")

def main():
    welcome_message()
    shapes = [
        Rectangle(5,8),
        Circle(7),
        Triangle(6,4)
    ]
    for shape in shapes:
        shape.describe()
        area_cm2 = shape.area()
        area_m2 = shape.utils.convert_cm2_to_m2(area_cm2)
        print(f"That")
            
            
    bigger = utils.larger_shape(shapes[0], shapes[1])
    print("Between the first two shapes, the larger one is:") 
    bigger.describe()

if __name__ == "__main__":
    main()