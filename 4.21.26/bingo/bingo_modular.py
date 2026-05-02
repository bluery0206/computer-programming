# Libraries
import numpy as np

def get_random_letter():
    letters = ["B", "I", "N", "G", "O"]
    return letters[np.random.randint(0, 4)]

def determine_range(letter):
    min, max = 0, 0
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
    return min, max

def in_list(needle, haystack):
    return needle in np.array(haystack).flatten()

def main():
    letter = get_random_letter()
    min, max = determine_range(letter)
    number = np.random.randint(min, max)

    print(f"Numero {number} sa letrang {letter}")

    bingo = [
        # B     I       N       G       O
        [12,    16,     31,     48,     61],
        [1,     28,     35,     59,     75],
        [5,     24,     None,   49,     65],
        [8,     26,     44,     46,     67],
        [10,    25,     40,     47,     63],
    ]

    if in_list(number, bingo):
        print(f"NAA KOY {number}")

if __name__ == "__main__":
    main()