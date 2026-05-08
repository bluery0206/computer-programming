# This program will have
#   - add student
#   - edit student
#   - delete studnet
#   - view student

# libraries
import random # for methods that generate random characters
import string # for string related method ie get all the letters

# sudlanan sa students
# it is a list with dictionaries as items
# so in the program, ngani iyang porma supposedly
# example as empty:
#      [ {}, {}, {}, ]
#   where each {} represents a student with information inside the dict
# 
# example
#       [
#           { 
#               "first_name"    : "Juan",
#               "last_name"     : "Dela Cruz",
#               "address"       : "Inabanga, Bohol",
#               "age"           : 23,
#               "year_level"    : 1,
#           },
#           { 
#               "first_name"    : "Pedro",
#               "last_name"     : "Penduko",
#               "address"       : "Clarin, Bohol",
#               "age"           : 23,
#               "year_level"    : 2,
#           },
#       ]
#   so we can access each student via
#       student = student_list[0]
#   and access the students info via
#       student['first_name']
student_list:list[dict] = []


def display_header(title:str) -> None:
    """ Para effects lang """
    print()
    print("=====================================")
    print(title.upper()) # PARA DAKO ANG TITLE
    print("=====================================")


def get_command():
    """
        literally to get the command
        but automatic removal of extra space at the beginning or at the end of the command
        and convert it to lowercase para dile na kaayo hassle
    """
    print()
    # .strip() removes spaces before and after the word
    return input(">>> ").strip().lower()


def display_commands():
    display_header("COMMANDS")

    print("exit \t\tTo exit the program")
    print("commands \tTo display comamnds")
    print("students \tTo display students")
    print("add student \tTo add new student")
    print("edit student \tTo edit new student")
    print("delete student \tTo delete new student")


def display_student(student: dict):
    full_name = student['first_name'] + " " + student['last_name']
    print(f"ID: {student['id']}, Name:{full_name}, Age:{student['age']}, Address:{student['address']}, Year Level:{student['year_level']}")


def display_students():
    display_header("STUDENTS")

    if len(student_list) == 0:
        print("There are no students")
    else:
        for student in student_list:
            display_student(student)


def  generate_id():
    """ 
        generates set of 4 random characters
        you can skip this one since this is kinda complicated
    """
    # generating the ID of the student
    # by generating a set of random characters
    length = 4
    #                  select random in     all numbers  and uppercase letters with lentgh of 4
    random_character_list = random.choices(string.digits  +   string.ascii_uppercase,     k=length)

    # combine/join all items in random_character_list separated by "" or nothing 
    return "".join(random_character_list)


def add_student():
    data = {
        "id"            : generate_id(),
        "first_name"    : input("First Name: "),
        "last_name"     : input("Last Name: "),
        "address"       : input("Address: "),
        "age"           : input("Age: "),
        "year_level"    : input("Year Level: "),
    }

    # Kada field sa dictionary,
    # if ang usa is empty, dile ipadayun ug insert
    for key in data:
        # .strip() removes spaces before and after the word
        if len(data[key].strip()) == 0:
            display_header("ERROR ADDING STUDENT")
            print(f"{key} is required.")
            return

    student_list.append(data)
    display_header("ADD STUDENT SUCCESSFUL")


def edit_student():
    display_header("EDIT STUDENT")

    if len(student_list) == 0:
        print("There are no students to edit")
    else:
        # .strip() removes spaces before and after the word
        id = input("Enter student ID to edit: ").strip().upper()
        
        for student in student_list:
            if student["id"] == id:
                display_student(student)
                key = input("Enter key to change (first_name, last_name, address, age, year_level): ").strip().lower()
                val = input(f"Enter value to change (old: {student[key]}): ").strip()

                student[key] = val
                display_header("EDIT STUDENT SUCCESSFUL")
                return
        else:
            print("No student with such ID exist.")


def delete_student():
    display_header("DELETE STUDENT")

    if len(student_list) == 0:
        print("There are no students to delete")
    else:
        id = input("Enter student ID to delete: ").strip().upper()
        
        # enumerate() converts a list into a tuple of (idx, value)
        # so it reutrns [ ( idx, {} ), ( idx, {} ), ... ]
        for idx, student in enumerate(student_list):
            if student["id"] == id:
                student_list.pop(idx)
                display_header("DELETE STUDENT SUCCESSFUL")
                return
        else:
            print("No student with such ID exist.")


def main():
    # during startup, display and command
    display_commands()

    # Murag loop() sa arduino
    while True:
        command = get_command()
        
        if command == "exit":
            break
        elif command == "commands":
            display_commands()
        elif command == "students":
            display_students()
        elif command == "add student":
            add_student()
        elif command == "edit student":
            edit_student()
        elif command == "delete student":
            delete_student()
        else:
            print("Unknown command.")
            display_commands()

if __name__ == "__main__":
    main()
