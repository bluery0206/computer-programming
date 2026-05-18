from student import Student
from course import Course

class Section:
    def __init__(self, name):
        self.name = name

        self.students = []

    def add_student(self, student):
        self.students.append(student)

if __name__ == "__main__":
    cc102 = Course("CC102", "Computer Programming 1", 2, 1)
    cc103 = Course("CC103", "Computer Programming 2", 2, 1)

    stud_1 = Student("Juan", "Dela Cruz")
    stud_2 = Student("Jade", "Reyes")
    stud_3 = Student("Aori", "Kasumi")

    section_1a = Section("1A")
    section_1a.add_student(stud_1)
    section_1a.add_student(stud_2)
    section_1a.add_student(stud_3)
    print(section_1a.students)