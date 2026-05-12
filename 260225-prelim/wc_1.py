def get_grade(score: int|float):
    if score >= 75:
        return "passed"
    elif score < 75:
        return "failed"
print(get_grade(90))
