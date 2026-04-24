# Multi-dimensional lists
# outer_list -> students_list
# inner_list -> students_information
#               0: full_name, 
#               1: age, 
#               2: year_and_section
students = [ 
    ["Ryan Hilario", 23, "BSIS-1D"],   # 0
    ["Jose Rizal", 30, "BSIS-1D"],      # -1
]

# ======================================================
# Add a new information inside of the last student
students[-1].append("Calamba")

# ======================================================
# KASABUTAN
# When adding a new student, we need to add a 
#       list of the student's information

# via append
students.append(["Maria Clara", 22, "BSIS-1D"])

# via insert
students.insert(0, ["Maria Clara", 22, "BSIS-1D"])

# ======================================================
# Convert the last student's full name to title case
students[-1][0].title()

print( students )
