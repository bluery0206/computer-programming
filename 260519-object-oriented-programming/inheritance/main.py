
class User:
    def __init__(self, username, password, age):
        self.username = username
        self.password = password
        self.age = age

    def display_all_properties(self):
        print(self.username, self.password, self.age)

user_1 = User("ngan", "pasurd", 23) # object creation
user_1.display_all_properties()
# method nga iprint tanang values