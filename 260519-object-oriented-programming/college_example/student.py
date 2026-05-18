# imports just for generating the student id
import random
import string

# imports for the classes we created
from course import Course

class Student:
    def __init__(self, fname, lname):
        # calls a function during object creation
        self.id = self.generate_id() 

        self.fname = fname 
        self.lname = lname
        
        self.courses = []

    def generate_id(self):
        return random.choices(string.ascii_uppercase + string.digits, k=4)

    def enroll(self, course: Course):
        self.courses.append(course)
        print(f'{self.full_name} has enrolled in {course.name}')

    # @property makes a method behave like a property 
    # so that we can access it by doing `method_name` instead of `method_name()`
    # like a property!
    @property 
    def full_name(self):
        return f"{self.fname} {self.lname}"

    # __str__ and __repr__ methods are just here so that it returns
    # its full_name instead of [<course.Course object at 0x00000255534B97F0>]
    # when we print the object itself
    def __str__(self):
        return self.full_name

    def __repr__(self):
        return self.full_name

if __name__ == "__main__":
    cc102 = Course("CC102", "Computer Programming 1", 2, 1)
    cc103 = Course("CC103", "Computer Programming 2", 2, 1)

    stud_1 = Student("Juan", "Dela Cruz")
    stud_1.enroll(cc102)
    stud_1.enroll(cc103)
    print(stud_1.courses)