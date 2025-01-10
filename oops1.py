# Initiate a class
class employee:
    # Special method/magic method/dunder method - constructor(it called first when obj calls)
    def __init__(self):
        print("Started executing attributes/data")
        self.id = 123
        self.salary = 50000
        self.designation = "SDE"
        print("attributes/data have been initiated")
    # Adding methods
    def travel(self, destination):
        print("This travel method was calling manually")
        print(f"Employee is now travelling to {destination}")

# create an obj/instance of the class 
sam = employee()
# Printing attributes
print(sam.salary)
print(sam.id)
# Calling a methodclear
sam.travel("Mumbai")
