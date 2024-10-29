menu = {"popcorn": 6.00,
        "coke": 2.25,
        "water": 1.15,
        "nachos": 4.45,
        "chips": 3.30,
        "icetea": 2.15}

cart = []
total = 0

print(f"{'-' * 10} menu {'-' * 10}")
for key, value in menu.items():
    print(f"{key:10}: ${value:.2f}")
print("-" * 27)

while True:
    food = input("select an item (q to quit): ").lower()
    if food == "q":
        break
    elif menu.get(food) is not None:
        cart.append(food)

print(f"{'-' * 7} your order {'-' * 7}")
for food in cart:
    total += menu.get(food)
    print(food, end=" ")

print()
print(f"total is: ${total:.2f}")
print(f"{'-' * 27}")