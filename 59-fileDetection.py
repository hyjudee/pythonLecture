import os

file_path = "C:/user/HP/Desktop/test"

if os.path.exists(file_path):
    print(f"the location '{file_path}' exists")

    if os.path.isfile(file_path):
        print("that is a file")
    elif os.path.isidr(file_path):
        print("that is a directory")

else:
    print("that location doesn't exist")