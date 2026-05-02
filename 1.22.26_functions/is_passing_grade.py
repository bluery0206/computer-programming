# Write a code that asks the user
# for a grade and then prints
# if the user passed the course
# passing is 75

# nakapasar_or_wala
# function to get user input
def is_passing_grade ():
    grade = int(input("Enter grade: "))

    if grade > 74:
        print("You passed!")
    else:
        print("You failed!")

is_passing_grade()