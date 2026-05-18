class Student:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname
        self.courses = []

    def enroll(self, course_name:str):
        self.courses.append(course_name)
        print(f'{self.fname} {self.lname} has enrolled in {course_name}')