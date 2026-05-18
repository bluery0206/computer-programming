students = [
    {
        'first_name': 'Juan', 
        'last_name': 'Dela Cruz',
        'courses': ['CC103', 'Val-Ed2']
    },
    {
        'first_name': 'Jade', 
        'last_name': 'Reyes',
        'courses': ['CC103', 'Val-Ed2']
    }
]

# printing all students
print(students)

# accessing the first student
print(students[0])
# prints {'first_name': 'Juan', 'last_name': 'Dela Cruz', 'courses': ['CC103', 'Val-Ed2']} 

# accessing the first student's first name
print(students[0]['first_name'])
# prints 'Juan'

# accessing the first student's courses
print(students[0]['courses'])
# prints ['CC103', 'Val-Ed2']

# accessing the first student's first course
print(students[0]['courses'][0])
# prints ['CC103', 'Val-Ed2']

# updating the first name of the first student;
students[0]['first_name'] = 'Juanito'
print(students[0])
# prints {'first_name': 'Juanito', 'last_name': 'Dela Cruz', 'courses': ['CC103', 'Val-Ed2']}





# STORINGG IN VARIABLES INSTEAD OF PRINTING DIRECTLY
student_1 = students[0]
# returns {'first_name': 'Juan', 'last_name': 'Dela Cruz', 'courses': ['CC103', 'Val-Ed2']} 

fname_1 = student_1['first_name']   
# returns 'Juan'

courses_1 = student_1['courses']      
# returns ['CC103', 'Val-Ed2']

first_course_1 = courses_1[0]              
# returns 'CC103'

