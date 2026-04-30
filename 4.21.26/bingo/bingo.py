# Libraries
import random

letters = ["B", "I", "N", "G", "O"]

letter = letters[random.randint(0, 4)]

min = 0
max = 0

# Determine the range of numbers based on the letter
if letter == "B":
    min = 1
    max = 15
elif letter == "I":
    min = 16
    max = 30
elif letter == "N":
    min = 31
    max = 45
elif letter == "G":
    min = 46
    max = 60
elif letter == "O":
    min = 61
    max = 75

number = random.randint(min, max)
print(f"Numero {number} sa letrang {letter}")

bingo = [
    # B     I       N       G       O
    [12,    16,     31,     48,     61],
    [1,     28,     35,     59,     75],
    [5,     24,     None,   49,     65],
    [8,     26,     44,     46,     67],
    [10,    25,     40,     47,     63],
]

for row in bingo:
    if number in row:
        print(f"NAA KOY {number}")