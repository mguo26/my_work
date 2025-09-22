def cm2_to_m2(area_cm2):
    """
    Convert an area from cm^2 to m^2.

    Parameters:
        area_cm2 (float): area in square centimeters

    Returns:
        float: area in square meters
    """
    return area_cm2 / 10000

def compare_areas(shape1, shape2):
    """
    Compare the areas of two shapes and print which is larger.

    Parameters:
        shape1, shape2: any objects with an area() method
    """
    a1 = shape1.area()
    a2 = shape2.area()
    if a1 > a2:
        print("First shape is larger")
    elif a2 > a1:
        print("Second shape is larger")
    else:
        print("Both shapes have the same area")
