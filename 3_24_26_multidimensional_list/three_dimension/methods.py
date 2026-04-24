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
sections = [ 
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
    ],
]

# When adding new section, we need to add a new list of 
#   students
sections.append( [ ["Jose Rizal", 32] ] )

print( sections )
