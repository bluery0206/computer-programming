def get_grade(score:int|float):
    if score >= 75:
        return "Passed"
    elif score < 75:
        return "Failed"
print(get_grade(90))
