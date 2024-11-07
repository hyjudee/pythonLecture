class shape:
    def __init__(self, colour, is_filled):
        self.colour = colour
        self.is_filled = is_filled
    
    def describe(self):
        print(f"it is {self.colour} and {'filled' if self.is_filled else 'not filed'}")

class circle(shape):
    def __init__(self, colour, is_filled, radius):
        super().__init__(colour, is_filled)
        self.radius = radius
    
    def describe(self):
        super().describe()
        print(f"it's {3.14 * self.radius * self.radius}cm^2")

class square(shape):
    def __init__(self, colour, is_filled, width):
        super().__init__(colour, is_filled)
        self.width = width

    def describe(self):
        super().describe()
        print(f"it's {self.width * self.width}cm^2")


class triangle(shape):
    def __init__(self, colour, is_filled, width, height):
        super().__init__(colour, is_filled)
        self.width = width
        self.height = height

    def describe(self):
        super().describe()
        print(f"it's {self.width * self.height / 2}cm^2")


circle = circle(colour="red", is_filled=True, radius=5)
square = square("blue", False, 6)
triangle = triangle("yellow", True, 7, 8)

print(circle.colour)
print(square.is_filled)
print(triangle.width)
print(f"{triangle.width}cm")
circle.describe()