# This is a simplified version of the bingo game.

# Libraries
import random

# Remember that strings are also lists of characters, 
# so we can access them using an index
# In here, B will have the index of 0, and so on.
bingo_letters ="BINGO"

# In bingo, as you guys explained it to me, have rules
# per letters in bingo, there will be different range
# of numbers nga igenerate sa column
#   B = 1-15
#   I = 16-30
#   N = 31-45
#   G = 46-60
#   O = 61-75

# But how do we generate a random number and know what letter it belongs to?
# We have two approach in mind to do this
#   1. Choose random number from 1 to 75 first, then we will check if
#        the number is in the range or between the min and max of the letter
#   2. Choose a random letter first then
#       generate a random number based on the letter's range

# In this code we will be doing the first approach

# We will generate a random number from 1 to 75
number = random.randint(1, 75)

# Now that we have the number, we can determine the letter based on the number's range

# initialize the letter variable to an empty string, we will update this value
letter = ""

# We will check if the number is 
# in the range or between the min and max of the letter
if (number >= 1) and (number <= 15): letter = "B"
elif (number >= 16) and (number <= 30): letter = "I"
elif (number >= 31) and (number <= 45): letter = "N"
elif (number >= 46) and (number <= 60): letter = "G"
elif (number >= 61) and (number <= 75): letter = "O"

print(f"Numero {number} sa letrang {letter}")

bingo = [
    # B     I       N       G       O
    [12,    16,     31,     48,     61],
    [1,     28,     35,     59,     75],
    [5,     24,     None,   49,     65],
    [8,     26,     44,     46,     67],
    [10,    25,     40,     47,     63],
]

# for every row in bingo, we will check if the number is in the row
# and if it is, we will print that we have the number
for row in bingo:
    if number in row:
        print(f"NAA KOY {number}")