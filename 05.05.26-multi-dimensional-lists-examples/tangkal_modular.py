tangkal = [
    ["bisaya", "45 days"],
    ["45 days", "45 days"],
    ["bisaya", "bisaya", "bisaya", "bisaya", "bisaya"],
    ["bisaya", "bisaya", "bisaya", ]
]

def get_command(message = "\nEnter command (count, display, exit): "):
    return input(message).strip().lower()

def count_manok(manok):
    count = 0
    for lugwa in tangkal:
        count = count + lugwa.count(manok)
    return count

def display_tangkal():
    for i, lugwa in enumerate(tangkal):
        print(f"Lugwa {i + 1}: {lugwa}")

while True:
    command = get_command()

    if command == "exit": 
        break
    elif command == "count":
        manok = get_command("Enter the manok name to count: ")
        count = count_manok(manok)
        print(f"Naa kay {count} kabuok manok nga {manok} sa tangkal.")
    elif command == "display":
        display_tangkal()
    else:
        print("Invalid command. Please try again.")