# Multi-dimensional lists

# list of first_year students
# grouped by their section
# each student has their own information 
#           (full name, age, year and section)

# KASABUTAN
# outer list: list of sections
# inner list: list of students in each section
# innermost list: information about each student
#            [0:full name, 1:age]
first_students_by_section = [ 
    [ 
        ["Ryan Hilario", 18], 
        ["Jane Doe", 19] 
    ],
    [ 
        ["Yuji Itadori", 21], 
        ["Jhon Wick", 34] 
    ],
    [ 
        ["Walter White", 43], 
        ["Jessie Pinkman", 23] 
    ]
]

# Update the age of the 1st student in 3rd section
first_students_by_section[2][0][1] = 53

print( first_students_by_section )
