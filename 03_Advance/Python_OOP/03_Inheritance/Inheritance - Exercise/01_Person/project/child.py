from project.person import Person


class Child(Person):

    def __init__(self, name=None, age=None):
        super(Child, self).__init__(name, age)

