class Course:
    def __init__(self, code, name, lab_units, lec_units, description = None):
        self.code = code
        self.name = name
        self.lab_units = lab_units
        self.lec_units = lec_units

        # not required but still accessible. it just returns None if wala gisupplyan
        self.description = description 

        # prerequisites are courses that students must pass before they can enroll the course
        self.prerequisites = []

    def add_prerequisite(self, course:Course):
        self.prerequisites.append(course)

    # __str__ and __repr__ methods are just here so that it returns
    # its name instead of [<course.Course object at 0x00000255534B97F0>]
    # when we print the object itself
    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name

if __name__ == "__main__":
    cc102 = Course("CC102", "Computer Programming 1", 2, 1)
    cc103 = Course("CC103", "Computer Programming 2", 2, 1)
    web101 = Course("WEB101", "Web Systems and Technologies", 2, 1)

    # If you want to be specific in what properties 
    # you are passing the arguments, you can specify it
    gec_art = Course(
        code = "GEC-Art", 
        name = "Art Appreciation", 
        lab_units = 3, 
        lec_units = 0
    )

    cc103.add_prerequisite(cc102)