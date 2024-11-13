# file_path = "output.txt"

# try:
#     with open(file_path, "r")as file:
#         content = file.read()
#         print(content)
# except FileNotFoundError:
#     print("that file was not found")
# except PermissionError:
#     print("you do not have permission to read that file")


# import json
# file_path = "output.json"

# try:
#     with open(file_path, "r")as file:
#         content = json.load(file)
#         print(content)
# except FileNotFoundError:
#     print("that file was not found")
# except PermissionError:
#     print("you do not have permission to read that file")


import csv
file_path = "output.csv"

try:
    with open(file_path, "r")as file:
        content = csv.reader(file)
        for line in content:
            print(line)
        print(content)
except FileNotFoundError:
    print("that file was not found")
except PermissionError:
    print("you do not have permission to read that file")
    