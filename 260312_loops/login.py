users = [
    {"username": "admin", "password": "1234", "role": "admin"},
    {"username": "student", "password": "abcd", "role": "student"}
]

print("=== Login System ===")

logged_in = False
logged_in_user = None

while not logged_in:

    username = input("Username: ")
    password = input("Password: ")

    for user in users:
        if user["username"] == username and user["password"] == password:
            logged_in = True
            logged_in_user = user
            break

    if logged_in:
        print("Login successful!\n")
    else:
        print("Invalid credentials\n")


while True:

    print("\n=== Main Menu ===")
    print("1. View Profile")
    print("2. Change Password")
    print("3. Logout")

    choice = input("Select option: ")

    if choice == "1":

        print("\n--- Profile ---")
        print("Username:", logged_in_user["username"])
        print("Role:", logged_in_user["role"])

    elif choice == "2":

        current_password = input("Enter current password: ")

        if logged_in_user["password"] == current_password:

            new_password = input("Enter new password: ")
            confirm_password = input("Confirm new password: ")

            if new_password == confirm_password:
                logged_in_user["password"] = new_password
                print("Password updated successfully!")
            else:
                print("Passwords do not match")

        else:
            print("Incorrect current password")

    elif choice == "3":

        print("Logging out...")
        break

    else:
        print("Invalid option")