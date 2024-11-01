# word = "apple"
# letter = input("guess a letter in the secret word: ")
# if letter in word:
#     print(f"there is a {letter}")
# else:
#     print(f"{letter} is not found")

# if letter not in word:
#     print(f"{letter} is not found")
# else:
#     print(f"there is a {letter}")

# students = {"chirs", "sandy", "anni"}
# student = input("enter the name of a student: ")
# if student in students:
#     print(f"{student} is in a class")
# else:
#     print(f"{student} is not in a class")

# if student not in students:
#     print(f"{student} is not in a class")
# else:
#     print(f"{student} is in a class")

# grades = {"chris": "a", 
#           "sandy": "c", 
#           "anni": "b"}
# student = input("enter the name of a student: ")
# if student in grades:
#     print(f"{student}'s grade is {grades[student]}")
# else:
#     print(f"{student} was not found")

email = "abc123@gmail.com"
if "@" in email and "." in email:
    print("valid email")
else:
    print("invalid email")
