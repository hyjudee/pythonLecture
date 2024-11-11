class Employee:

    def __init__(self, name, position):
        self.name = name
        self.position = position

    def get_info(self):
        return f"{self.name} = {self.position}"
    
    @staticmethod
    def is_valid_position(position):
        valid_positions = ["manager", "cashier", "cook", "janitor"]
        return position in valid_positions
    
employee1 = Employee("josh", "manger")
employee2 = Employee("jane", "cashier")

print(Employee.is_valid_position("cook"))
print(Employee.is_valid_position("sciientist"))

print(employee1.get_info())
print(employee2.get_info())

