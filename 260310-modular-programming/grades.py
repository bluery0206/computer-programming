def average_grade(grades):
    avg = sum(grades) / len(grades)
    return avg

# First sem
first_sem = [1.2, 1.1, 1.0,1.4, 3.0]

# Second Sem
second_sem = [3.0, 3.4, 3.2, 2.4, 2.5]

avg_first = average_grade(first_sem)
avg_second = average_grade(second_sem)
120
print(average_grade([avg_first, avg_second]))

