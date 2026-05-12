# ako rang gibalhin sa laing file ang list para dile kaayo cluttered and
# mafocus per use-case ang example
from students_by_section import students_by_section

# Printing all students regardless of section
# so tanan gyud
for section in students_by_section:
    for student in section['students']:
        print(f"{student['first_name']} {student['last_name']}")
