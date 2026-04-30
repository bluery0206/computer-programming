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

# In this code we will be doing second approach

# Get a random index from 0 to 4
#   letters: B  I   N   G   O
#   indexes: 0  1   2   3   4
random_index = random.randint(0, 4)

# Then based on the random selected index, we will get the letter
# from the bingo_letters string using the random index
letter = bingo_letters[random_index]

# Now that we have the letter, we can determine the range of numbers based on the letter

# But first let's initialize the min and max variables to 0,
# we will update these values based on the letter
min, max = 0, 0
# We can also write this in one line the first 0 will 
# be assigned to min and the second 0 will be assigned to max

# Determine the range of numbers based on the letter
if letter == "B": min, max = 1, 15
elif letter == "I": min, max = 16, 30
elif letter == "N": min, max = 31, 45
elif letter == "G": min, max = 46, 60
elif letter == "O": min, max = 61, 75

# Now that we have the letter and the range of numbers, we can now
# generate a random number based on the letter's range using 
# the random.randint() function, we will pass the min and max as arguments
# for example if the letter is B, we will generate a random number with 
# the minimum number of 1 and the maximum number of 15
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

# for every row in bingo, we will check if the number is in the row
# and if it is, we will print that we have the number
for row in bingo:
    if number in row:
        print(f"NAA KOY {number}")