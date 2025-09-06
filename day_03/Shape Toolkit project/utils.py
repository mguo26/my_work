#          * Create helper functions, e.g., convert cm^2 to m^2
#          * Compare areas of two shapes

def convert_cm2_to_m2(area_cm2: float) :
    converted_value = area_cm2 / 10_000
    return converted_value

def larger_shape(shape1, shape2):
    if shape1.area()> shape2.area():
        return shape1
    else:
        return shape2
