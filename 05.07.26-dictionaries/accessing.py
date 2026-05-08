student = {
    "first_name" : "Juan",
    "last_name"  : "Dela Cruz",
    "address"    : "Poblacion, Inabanga, Bohol",
    "age"        : 20,
    "year_level" :  1,
}

print(student)

# ireturn ang value sa specified key (first_name)
print(f"First name: { student["first_name"] }")

# we can also access the index of the first name's letter
fname_first_letter = student["first_name"][0]
print(f"First letter of the first name: { fname_first_letter }")