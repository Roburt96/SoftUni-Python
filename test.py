class Dog:
    # class attribute
    __attr1 = "mammal"

    # Instance attribute
    def __init__(self, name):
        self.name = name

    @property
    def attribute(self):
        return self.__attr1

    @attribute.setter
    def attribute(self, value):
        if isinstance(value, str):
            self.__attr1 = value

# Driver code
# Object instantiation
Rodger = Dog("Rodger")
Tommy = Dog("Tommy")

# Accessing class attributes
print(f"Rodger is a {Rodger.attr1}")
print("Tommy is also a {}".format(Tommy.__class__.attr1))

# Accessing instance attributes
print("My name is {}".format(Rodger.name))
print("My name is {}".format(Tommy.name))