room = {
    "name": "Speechlab",
    "location": "2nd Floor, ICAS Bldg.",
    "n_computers": 24,
    "n_chairs": 25,
    "is_airconed": True
}

while True:
    command = input("command: ")

    if command == "exit":
        break

    elif command == "view":
        print(room)

    elif command == "update":
        print(f"keys: {room.keys()}")
        key = input("key: ")
        value = input("value: ")
        room[key] = value

    elif command == "add":
        key = input("key: ")
        value = input("value: ")

        room[key] = value 

    elif command == "remove":
        print(f"keys: {room.keys()}")
        key = input("key: ")
        room.pop(key)

    else:
        print("Invalid command.")