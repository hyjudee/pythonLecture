# fruits = ["apple", "orange", "banana"]
# vegies = ["celery", "carrots", "potatoes"]
# meat = ["chiken", "fish", "turkey"]

# groceries = [["apple", "orange", "banana"],
#              ["celery", "carrots", "potatoes"],
#              ["chiken", "fish", "turkey"]]

# groceries = [fruits, vegies, meat]

# print(groceries)
# print(groceries[0])
# print(groceries[0][2])

# for collection in groceries:
#     print(collection)

# for collection in groceries:
#     for food in collection:
#         print(food, end=" ")
#     print()


num_pad = ((1, 2, 3),
           (4, 5, 6),
           (7, 8, 9),
           ("*", 0, "#"))

# for row in num_pad:
#     print(row)

for row in num_pad:
    for num in row:
        print(num, end=" ")
    print()