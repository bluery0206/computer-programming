student_list = [
    {"name": "Juan", "section": "1A"},
    {"name": "Jade", "section": "1B"},
    {"name": "Jade", "section": "1C"},
    {"name": "Juan", "section": "1D"},
]

name_to_search = input("student delete: ")

for stud in student_list:
    if stud['name'] == name_to_search:
        student_list.remove(stud)
else:
    print("no student found")

print(student_list)
