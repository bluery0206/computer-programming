class Lugwa:
    def __init__(self, name):
        self.name = name

        self.manoks = []

    def add_manok(self, manok):
        self.manoks.append(manok)

    # __str__ and __repr__ methods are just here so that it returns
    # its name instead of [<course.Course object at 0x00000255534B97F0>]
    # when we print the object itself
    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name