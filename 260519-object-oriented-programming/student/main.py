class Student:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname
        self.courses = []

    def enroll(self, course_name):
        self.courses.append(course_name)
        print(f'{self.full_name} has enrolled in {course_name}')

stud_1 = Student(fname='Juan', lname='Dela Cruz')
stud_1.enroll('CC103')
print(stud_1.courses)

stud_1.idk = "Dsads"
print(stud_1.idk)
