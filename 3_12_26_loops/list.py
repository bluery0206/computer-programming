bag_items = [
    ["juan", False],
    ["manga", True],
    ["Moskov", False],
]

for item in bag_items:
    if item[1] == True:
        print(f"{item[0]} is a food")
    else:
        print(f"{item[0]} is not a food")
