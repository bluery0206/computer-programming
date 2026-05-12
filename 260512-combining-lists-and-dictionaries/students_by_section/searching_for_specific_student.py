# ako rang gibalhin sa laing file ang list para dile kaayo cluttered and
# mafocus per use-case ang example
from students_by_section import students_by_section

# Searching for a specific student
name_to_search = input("Enter student name to search: ")

# kay names arent unique to one person like "John" so we 
# store it in a list para makuha nato ang mga names nga 
# naay kapareho. this also allows us to show ug pila kabuok result
students_found = [] 

for section in students_by_section:
    for idx, student in enumerate(section['students']):
        # .find() returns -1 if the character is not found in the string
        # and returns the position/index of the character in the list if found
        # for example:
        #   let be our search word (name_to_search) be J
        #       "John".find("J")
        #   this returns 0

        # so we can decide that it is found if .find() returns 0 or above

        # it is like asking "Kinsay naay letter J sa ilang ngan?"
        # then those students raise their hands

        # name searches usually look for first and last name
        # but you can include other stuff such as suffix (jr), middle name, etc
        is_found_in_first_name  = student['first_name'].find(name_to_search) >= 0
        is_found_in_last_name   = student['last_name'].find(name_to_search) >= 0

        is_found =  is_found_in_first_name or is_found_in_last_name

        if is_found:
            # atong giappend ang dictionary sa found list
            students_found.append(student) 

if len(students_found) > 0:
    print(f"Found {len(students_found)} results.")

    for idx, student in enumerate(students_found):
        print(f"   {idx+1}. {student.get('first_name')} {student.get('last_name')}")
else:
    print("No student found.")