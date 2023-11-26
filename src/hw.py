import math

 #########  Oject-Oriented Approach #########
class Shape:
    def __init__(self, name):
        self.name = name

    def perimeter(self):
        raise NotImplementedError("perimeter")

    def area(self):
        raise NotImplementedError("area")
    
    def density(self, weight):
        raise weight/ self.area()
    

    
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
    

 ######### Dictionary Representation of Classes #########
# Circle

def circle_perimeter(thing):
    return 2 * math.pi * thing["radius"]

def circle_area(thing):
    return math.pi * thing["radius"] ** 2

def circle_larger(thing, size):
    return call(thing, "area") > size

# Instead of using classes directly, the code represents classes a dictionaries. These dictionaries contains keys for methods, class name('_classname'), and a refrences to the parent class('_parent') 
Circle = {
    "perimeter": circle_perimeter,
    "area": circle_area,
    "larger": circle_larger, 
    "_classname": "Circle",
    "_parent": Shape
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


# Instead of using classes directly, the code represents classes a dictionaries. These dictionaries contains keys for methods, class name('_classname'), and a refrences to the parent class('_parent') 
Square = {
    "perimeter": square_perimeter,
    "area": square_area,
    "larger": square_larger,
    "_classname": "Square",
    "_parent": Shape
}

def square_new(name, side):
    return {
        "name": name,
        "side": side,
        "_class": Square
    }


# Method Calling

def call(thing, method_name, *args):
    method = find(thing["_class"], method_name)
    return method(thing, *args)

def find(cls, method_name):
    while cls is not None:
        if method_name in cls:
            return cls[method_name]
        cls = cls["_parent"]
    raise NotImplementedError("method_name")


examples = [square_new("sq", 4), circle_new("ci", 2)]
for ex in examples:
    n = ex["name"]
    p = call(ex, "perimeter")
    a = call(ex,"area")
    c = ex["_class"]["_classname"]
    result = call(ex, "larger", 10)
    # print(f"is {ex['name']} larger? {result}")
    # print(f"{n} is a {c}: {p:.2f} {a:.2f}")



def shape_density(thing, weight):
    return weight / call(thing, "area")
    

Shape = {
    "density": shape_density,
    "_classname": "Shape",
    "parent": None
}
