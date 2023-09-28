class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_name(self):
        return self.name


b = Dog("layke", 5)
c = b.get_name()
print(c)
