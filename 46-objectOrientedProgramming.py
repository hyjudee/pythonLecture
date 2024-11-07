class car:
    def __init__(self, model, year, colour, for_sale):
        self.model = model
        self.year = year
        self.colour = colour
        self.for_sale = for_sale

    def drive(self):
        print(f"you drive the {self.colour} {self.model}")

    def stop(self):
        print(f"you stop the {self.colour} {self.model}")

    def describe(self):
        print(f"{self.year} {self.colour} {self.model}")

car1 = car("jeep", 2022, "red", False)
car2 = car("bmw", 2020, "gray", True)

print(car2.model)
print(car1.colour)
print(car1.for_sale)

car1.drive()
car2.stop()

car1.describe()
