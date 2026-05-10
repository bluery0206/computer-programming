# ako rang gibalhin sa laing file ang list para dile kaayo cluttered and
# mafocus per use-case ang example
from students_by_section import students_by_section

# Printing all students per section
for section in students_by_section:
    print(section['name'])
    # enumerate() converts a list into a list of tuples
    # example: 
    #     original_list = ["A", "B", "C", "D"]
    #     new_list = enumerate(original_list)
    #     
    #     newlist now have:
    #           [(0, "A"), (1, "B"), (2, "C"), (3, "D")]
    #
    # and now when iterating, we get one item
    # so in the first iteration, we get
    #   0 and "A"
    # in here below, we are just extracting those values
    # by using two variables: idx & student where:
    #   - 0 would be stored in idx
    #   - "A" would be stored in student
    for idx, student in enumerate(section['students']):
        # idx + 1 kay zero man start sa idx and weird sad if 0 ta magstart sa listahan
        print(f"    {idx+1}. {student['first_name']} {student['last_name']}")
