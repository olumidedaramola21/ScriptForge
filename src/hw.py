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


# Circle

def circle_perimeter(thing):
    return 2 * math.pi * thing["radius"]

def circle_area(thing):
    return math.pi * thing["radius"] ** 2

def circle_larger(thing, size):
    return call(thing, "area") > size

Circle = {
    "perimeter": circle_perimeter,
    "area": circle_area,
    "larger": circle_larger, 
    "_classname": "Circle"
}

def circle_new(name, radius):
    return {
        "name": name,
        "radius": radius,
        "_class": Circle
    }


# square

def square_perimeter(thing):
    return 4 * thing["side"]

def square_area(thing):
    return thing["side"] ** 2

def square_larger(thing, size):
    return call(thing, "area") > size

Square = {
    "perimeter": square_perimeter,
    "area": square_area,
    "larger": square_larger,
    "_classname": "Square"
}

def square_new(name, side):
    return {
        "name": name,
        "side": side,
        "_class": Square
    }



def call(thing, method_name, *args):
    return thing['_class'][method_name](thing, *args)

examples = [square_new("sq", 4), circle_new("ci", 2)]
for ex in examples:
    n = ex["name"]
    p = call(ex, "perimeter")
    a = call(ex,"area")
    c = ex["_class"]["_classname"]
    result = call(ex, "larger", 10)
    print(f"is {ex['name']} larger? {result}")
    # print(f"{n} is a {c}: {p:.2f} {a:.2f}")


# ARGUMENTS
# Varags
# def show_args(title, *args, **kwargs):
#     print(f"{title} args '{args}' and kwargs '{kwargs}'")

# show_args("nothing")
# show_args("one unnamed argument", 1)
# show_args("one named argumnet", second="2")
# show_args("one of each", 3, fourth= "4")

# Spreading
# def show_spread(left, middle, right):
#     print(f"left {left} middle {middle} right {right}")

# all_in_list = [1, 2, 3]
# # show_spread(*all_in_list)

# all_in_dict = {"right": 30, "left": 10, "middle": 20}
# # show_spread(**all_in_dict)
