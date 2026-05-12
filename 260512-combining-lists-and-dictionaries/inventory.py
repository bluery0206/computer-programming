inventory = [
    {"name": "Potion", "quantity": 5},
    {"name": "Sword", "quantity": 1},
]

def view_items():
    for item in inventory:
        print(f"Name: {item['name']}, Quantity: {item['quantity']}")

def add_item(name, quantity):
    data = {
        "name": name,
        "quantity": quantity,
    }

    inventory.append(data)
    print(f"{name} added in inventory.")

def decrease_quantity(name):
    for item in inventory:
        if item['name'] == name:
            original_quantity = item['quantity']

            if item["quantity"] == 0:
                print(f"Cannot decrease {item['name']} quantity. Already zero.")
            else:
                new_quantity = original_quantity - 1

                item['quantity'] = new_quantity
                print(f"{item['name']} quantity decreased from {original_quantity} to {new_quantity}")

def main():
    view_items()
    add_item("as", 2)
    decrease_quantity("as")
    decrease_quantity("as")
    decrease_quantity("as")

if __name__ == "__main__":
    main()