# from os import path
#
# if path.exists("example.txt"):
#     print("File found")
# else:
#     print("File is not found")
try:
    with open("example.txt") as file:
        print("File found")
except FileNotFoundError:
    print("File not found")
