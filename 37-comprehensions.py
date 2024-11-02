# doubles = []
# for x in range(1, 11):
#     doubles.append(x *2)
# print(doubles)

# doubles = [x * 2 for x in range(1, 11)]
# tripple = [y * 3 for y in range(1, 11)]
# print(doubles)
# print(tripple)

# fruits = ["apple", "orange", "banana"]
# fruits = [fruit.upper() for fruit in fruits]
# fruits_chars = [fruit[0] for fruit in fruits]
# print(fruits_chars)

# numbers = [1, -2, 3, -4, 5]
# postive_nums = [num for num in numbers if num >= 0]
# negative_nums = [num for num in numbers if num < 0]
# even_nums = [num for num in numbers if num % 2 == 0]
# odd_nums = [num for num in numbers if num % 2 == 1]
# print(odd_nums)

grades = [89, 43, 98, 56, 74]
passing_grades = [grade for grade in grades if grade >= 60]
print(passing_grades)