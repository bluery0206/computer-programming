# ako rang gibalhin sa laing file ang list para dile kaayo cluttered and
# mafocus per use-case ang example
from students_by_section import students_by_section

for section in students_by_section:
    print(section['name'])
    for student in section['students']:
        print(f"   {student['first_name']} {student['last_name']}")

student_name_to_delete = input("Enter exact student name to delete: ")
for section_idx, section in enumerate(students_by_section):
    for student_idx, student in enumerate(section['students']):
        full_name = f"{student['first_name']} {student['last_name']}" 

        if student_name_to_delete == full_name:
            section['students'].pop(student_idx)
            print(f"{full_name} has been removed.")
            break
