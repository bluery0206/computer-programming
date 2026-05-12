inventory = [
    # name      price   quantity
    ["gatas",   50,     10],
    ["tinapay", 20,     15],
    ["kape",    100,    5],
    ["asukal",  30,     20]
]

def update(name, column, value):
    for item in inventory:
        if item[0] == name:
            item[column] = value
            break

