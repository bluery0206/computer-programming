# Multi-dimensional lists
# outer_list -> students_list
# inner_list -> students_information
#               0: full_name, 
#               1: age, 
#               2: year_and_section
students = [ 
    ["Ryan Hilario", 23, "BSIS-1D"],   # 0
    ["Jose Rizal", 30, "BSIS-1D"]      # 1
]

# update first student's full_name
students[0][0] = "Mark Ryan Hilario"

print(students[0][0])
