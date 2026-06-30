class Student:
    def __init__(self):
        self.fname = ""
        self.lname = ""
        self.courses = []

    def add_course(self, course):
        # print("before:", self.courses)
        self.courses.append(course)
        # print("after:", self.courses)

    def display_all(self):
        print("fullname", self.fname, self.lname)
        print("corses:")

        for course in self.courses:
            print("-- ", course)

# object
student_1 = Student("ryan", "hilario")

student_1.add_course("CC103")
student_1.add_course("IS102")
student_1.add_course("WEB101")
# student_1.display_all()