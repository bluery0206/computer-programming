# per list sa class schedule represents the day of the week,
# so, naa tay class schedule nga naay 5 ka adlaw sa klase,
# and per adlaw, naay sud nga mga subjects
class_schedule = [
    ["NSTP2", 
        "STAT101", 
        "GEC-World", 
        "PATHFit 2", 
        "IS101"],
    ["GEC-Ethics", 
        "Val-Ed 2", 
        "GEC-Art", 
        "CC102"],
    ["NSTP2", 
        "STAT101", 
        "GEC-World", 
        "PATHFit 2", 
        "IS101"
    ],
    ["GEC-Ethics", 
        "Val-Ed 2", 
        "GEC-Art", 
        "CC102"
    ],
    ["NSTP2", 
        "STAT101", 
        "GEC-World", 
        "PATHFit 2", 
        "IS101"
    ],
]

# i print the first subject on the first day of class_schedule
print(class_schedule[0][0])

# ilisan ang first subject sa first day nga NSTP2 ug CC101
class_schedule[0][0] = "CC101"

# iphun ug kapila mu sud sa CC102 sa class_schedule
count = 0
for day in class_schedule:
    count = count + day.count("CC102")
print(f"Mu sud ang CC102 sa class_schedule ug {count} ka beses.")

