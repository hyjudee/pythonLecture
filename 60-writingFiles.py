# txt_data = "i like you"
# file_path = "output.txt"

# with open(file=file_path, mode="w") as file:
#     file.write(txt_data)
#     print(f"txt file '{file_path}' was created")

# try:
#     with open(file_path, "x") as file:
#         file.write(txt_data)
#         print(f"txt file '{file_path}' was created")
# except FileExistsError:
#     print("that file already exists!")

# try:
#     with open(file_path, "a") as file:
#         file.write("\n" + txt_data)
#         print(f"txt file '{file_path}' was created")
# except FileExistsError:
#     print("that file already exists!")


# employees = ["eric", "josh" "jenny"]
# file_path = "output.txt"

# try:
#     with open(file_path, "w") as file:
#         for employee in employees:
#             file.write(employee + "\n")
#         print(f"txt file '{file_path}' was created")
# except FileExistsError:
#     print("that file already exists!")


# import json
# employee = {
#     "name": "solar",
#     "age": 29,
#     "job": "singer"
# }
# file_path = "output.json"

# try:
#     with open(file_path, "w") as file:
#         json.dump(employee, file, indent=4)
#         print(f"json file '{file_path}' was created")
# except FileExistsError:
#     print("that file already exists!")


import csv
employees = [["name", "age", "job"],
             ["eric", 40, "singer"],
             ["josh", 22, "studnet"],
             ["jenny", 28, "cook"]]
file_path = "output.csv"

try:
    with open(file_path, "w", newline="") as file:
        writer = csv.writer(file)
        for row in employees:
            writer.writerow(row)
        print(f"csv file '{file_path}' was created")
except FileExistsError:
    print("that file already exists!")
    