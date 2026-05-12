student = {
    "first_name" : "Juan",
    "last_name"  : "Dela Cruz",
    "address"    : "Poblacion, Inabanga, Bohol",
    "age"        : 20,
    "year_level" :  1,
}

# ireturn ang value sa specified key (first_name)
# and unlike kadtong student['key'], kani siya if wala magexist ang key, None ra iyang ireturn
# so dile siya mag error
print(student.get("awaw"))

# returns the value of the specified key (middle_name)
# then if the key is not found, maginsert ug new nga key: value pair
# and return the value, passed as an argument
print(student.setdefault("middle_name", "N/A"))
# so in this case, ang mereturn is "N/A"

# iremove ang last key-value pair sa dictionary
# same sa pop sa list, pero igo ra gyud siya tangtang sa last key-value pair
# then after tangtangon, i return ang key-value pair nga na remove
print(student.popitem())
# output:
# ('year_level', 1)


# iremove ang key-value pair nga "age" : 20
# then i return ang value nga 20
print(student.pop("age"))


# returns a list of the dictionary's values
print(student.values())
# output:
# ['Juan', 'Dela Cruz', 'Poblacion, Inabanga, Bohol', 20, 1]

# returns a list of the dictionary's keys
print(student.keys())
# output:
# ['first_name', 'last_name', 'address', 'age', 'year_level']

# returns a list of the dictionary's key-value pairs as tuples
# tuple is another data type in python, it is similar to a list 
# but it is immutable meaning, dile mausab so dile
# ta pwede mag add or remove items sa tuple
print(student.items())

# returns a new dictionary with the specified keys and value
# ang keys kay "stud_1" ug "stud_2" then
# ang value sa tanan kay "Juan"
print(student.fromkeys(["stud_1", "stud_2"], "Juan"))
# output 
# {'stud_1': 'Juan', 'stud_2': 'Juan'}
