# akong giseparate ug file and list para dile cluttered ang
# code since naay mga explanations man 
# and if youre going to do the same, your folder must have
# at least an empty __init__.py in it
from student_list import student_list

print("============================")
print("STUDENT INFORMATION")
print("============================")

# EXPLANATION ON THE "attr" part
# .items() method returns a list of tuples
# 
#   example as empty: 
#       [(), (), ()]
#
#   example w/ placeholders:
#       [(key, value), (key, value), (key, value), ... ]
#
#   example w/ values from student dict: 
#       [("first_name", "Juan"), ("last_name", "Dela Cruz"), ... ]
# 
# and remember that when where iterating, per iteration, 
# atong gikuha ang usa ka item sa list and therefore, 
# naa na tay (key, value) sa atong current iteration variable nga si `attr`
# 
# Then kanang murag list pero naka parenthesis is a tuple datatype
# which acts like a list but immutable, meaning dile pedee mausab but 
# pede ta makaaccess just like what has been done per iteration:
# giaasign si first index as key and giassign si second index as val
for attr in student_list.items():
    key = attr[0]
    val = attr[1]
    print(f"{key.title()} : {val}")

print("============================")