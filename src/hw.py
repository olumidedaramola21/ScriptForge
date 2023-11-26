import math

class Shape:
    def __init__(self, name):
        self.name = name

    def perimeter(self):
        raise NotImplementedError("perimeter")

    def area(self):
        raise NotImplementedError("area")
    
class Square(Shape):
    def __init__(self, name, side):
        super().__init__(name)
        self.side = side

    def perimeter(self):
        return 4 * self.side
    
    def area(self):
        return self.side ** 2
    
class Circle(Shape):
    def __init__(self, name, radius):
        super().__init__(name)
        self.radius = radius

    def perimeter(self):
        return 2 * math.pi * self.radius
    
    def area(self):
        return math.pi * self.radius ** 2
    
examples = [Square("sq", 3), Circle("ci", 2)]
for thing in examples:
    n = thing.name
    p = thing.perimeter()
    a = thing.area()
    # print(f"{n} has perimeter {p:.2f} and area {a:.2f}")


# def square_perimeter(thing):
#     return 4 * thing["side"]

# def square_area(thing):
#     return thing["side"] ** 2

# def square_new(name, side):
#     return {
#         "name": name,
#         "side": side,
#         "perimeter": square_perimeter,
#         "area": square_area
#     }

# def circle_perimeter(thing):
#     return 2 * math.pi * thing["radius"]

# def circle_area(thing):
#     return math.pi * thing["radius"] ** 2

# def circle_new(name, radius):
#     return {
#         "name": name,
#         "radius": radius,
#         "perimeter": circle_perimeter,
#         "area": circle_area
#     }

# # If you want to use methods in this dictionary, we call it like this
# def call(thing, method_name):
#     return thing[method_name](thing)

# exam = [square_new("sq", 3), circle_new("ci", 2)]
# for ex in exam:
#     n = ex["name"]
#     p = call(ex, "perimeter")
#     a = call(ex, "area")
#     print(f"{n} {p:.2f} {a:.2f}")


def square_perimeter(thing):
    return 4 * thing["side"]

def square_area(thing):
    return thing["side"] ** 2

Square = {
    "perimeter": square_perimeter,
    "area": square_area,
    "_classname": "Square"
}

def square_new(name, side):
    return {
        "name": name,
        "side": side,
        "_class": Square
    }