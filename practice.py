# exercise 1 rectangle area calc
# length = float(input("Enter the length: "))
# width = float(input("Enter the width: "))
# area = length * width

# print(f"The area is: {area}cmª")

# exercise 2 shopping cart program
# item = input("what iteam would you like to buy?: ")
# price = float(input("what is the price?: "))
# quantity = int(input("how many would you like?: "))
# total = price * quantity

# print(total)
# print(f"your total price is: ${total}")


# madlibs game
# word game where you can create a story
# by filling in blanks with random words
# adjective1 = input("enter an adjective: ")
# noun1 = input("enter a place: ")
# adjective2 = input("enter what you were doing: ")
# adjective3 = input("enter how you felt about it: ")

# print(f"Today i went to a {adjective1} {noun1}")
# print(f"in the {noun1}, I was {adjective2}")
# print(f"{adjective2} was {adjective3}")


# import math
# radius = float(input("enter the radius a circle: "))
# circumference = 2 * math.pi * radius
# print(f"The circumference is : {round(circumference, 2)}cm")

# radius = float(input("enter the radius: "))
# area = math.pi * pow(radius, 2)
# print(f"the area is: {round(area, 2)}cm")

# a = float(input("enter side a: "))
# b = float(input("enter side b: "))
# c = math.sqrt(pow(a, 2) + pow(b, 2))

# print(f"the side c is {c}")
# print(f"the side c is {round(c, 2)}")


# age = int(input("enter your age: "))
# if age >= 18:
#    print("you are now signed up!")
# elif age < 0:
#    print("you haven't been born yet") 
# else:
#    print("you must be 18+ to sign up!")


# response = input("would you like food? (Y/N): ")
# if response == "Y":
#    print("i like you too")
# else:
#    print("i don't like you either")


# operator = input("enter an operator (+, -, *, /): ")
# num1 = float(input("enter the 1st number: "))
# num2 = float(input("enter the 2nd number: "))

# if operator == "+":
#    result = num1 + num2
#    print(result)
# elif operator == "-":
#    result = num1 - num2
#    print(result)
# elif operator == "*":
#    result = num1 * num2
#    print(result)
# elif operator == "/":
#    result = num1 / num2
#    print(result)
# else:
#    print(f"{operator} is not a valid operator")


# weight = float(input("enter your weight: "))
# unit = input("kg or pound? (K / L): ")

# if unit == "K":
#     weight = weight * 2.205
#     unit = "lbs."
#     print(f"your weight is: {round(weight, 1)} {unit}")
# elif unit == "L":
#     weight = weight / 2.205
#     unit = "kg."
#     print(f"your weight is: {round(weight, 1)} {unit}")
# else:
#     print(f"{unit} is not a valid")


# unit = input("is this temperature in celsius or fahrenheit? (C/F): ")
# temp = float(input("enter the temp: "))

# if unit == "C":
#     temp = round((9 * temp) / 5 + 32, 1)
#     print(f"the temp in °F is {temp}")
# elif unit == "F":
#     temp = round((temp - 32) * 5 / 9, 1)
#     print(f"the temp in °C is {temp}")
# else:
#     print(f"{unit} is an invalid unit of measurement")


# temp = 25
# is_raining = False
# if temp > 35 or temp < 20 or is_raining:
#     print("the outdoor event is cancelled")
# else:
#     print("the outdoor event is scheduled")

# temp = int(input("enter the temp: "))
# is_sunny = False

# if temp >= 28 and is_sunny:
#     print("it's hot outside")
#     print("it's sunny")
# elif temp <= 0 and is_sunny:
#     print("it's cold outside")
#     print("it's sunny")
# elif 28 > temp > 0 and is_sunny:
#     print("it's wamr outside")
#     print("it's sunny")
# elif temp >= 28 and not is_sunny:
#     print("it's hot outside")
#     print("it's cloudy")
# elif temp <= 0 and not is_sunny:
#     print("it's cold outside")
#     print("it's cloudy")
# elif 28 > temp > 0 and not is_sunny:
#     print("it's wamr outside")
#     print("it's cloudy")


# num = 5
# num = int(input("enter a number: "))
# # print("postive" if num > 0 else "negative")

# result = "even" if num % 2 == 0 else "odd"
# print(result)

# a = 6
# b = 7
# max_num = a if a > b else b
# min_num = a if a < b else b
# print(max_num)
# print(min_num)

# age = 25
# age = int(input("enter your age: "))
# status = "adult" if age >= 18 else "child"
# print(status)

# temp = 20
# weather = "hot" if temp > 25 else "cold"
# print(weather)

# user_role = "admin"
# access_level = "full access" if user_role == "admin" else "limited access"
# print(access_level)