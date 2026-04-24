def average(data):
    total   = sum(data)
    n_items = len(data)

    average = total / n_items

    return average

def main():
    avg = average([1, 2, 3])
    print(avg)

if __name__ == "__main__":
    main()