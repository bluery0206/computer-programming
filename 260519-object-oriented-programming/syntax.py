class ClassName:

    # runs when we create an objcet
    # ie:
    #   obj = ClassName("req arg")
    def __init__(self, req_param, another_param = "default value"):
        self.prop_one = req_param
        self.prop_two = another_param
        self.prop_three = "value"

    # self is a required parameter in methods
    def method_one(self):
        # some more code...
        print(self.prop_two)

    def method_two(self, req_param):
        # some more code...
        pass


obj_1 = ClassName("req arg")
obj_2 = ClassName("req arg", "optional arg")

# Each object can access all of the methods
obj_1.method_one()
obj_2.method_one()

# Each object contains their own data
print(obj_1.prop_one)
print(obj_2.prop_one)