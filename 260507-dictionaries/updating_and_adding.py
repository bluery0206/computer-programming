student = {
    "first_name" : "Juan",
    "last_name"  : "Dela Cruz",
    "address"    : "Poblacion, Inabanga, Bohol",
    "age"        : 20,
    "year_level" :  1,
}


# UPDATING
print("UPDATING")

print(f"original first_name : {student['first_name']}")

# to update values, we can use the keys
# so giaccess nato si first_name nga Juan
# then atong gitagaan ug new value by 
# assigning (=) it a new one
student['first_name'] = "John"
print(f"updated first_name  : {student['first_name']}")


print()  # print lang para naay space ang updating ug adding inag print

# ADDING
print("ADDING")

# this just gets the very last key: value pair in the list
print(f"original last element   : {next(reversed(student))}: {student[next(reversed(student))]}")

# to add a new key: value pair, simply
# use a nonexisting key and set its value
student['favorite_game'] = "Arknights"
print(f"new last element        : {next(reversed(student))}: {student[next(reversed(student))]}")
