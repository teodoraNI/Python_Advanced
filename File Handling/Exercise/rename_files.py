import os

directory = input("Enter a directory: ")
string_to_be_replaced = input("Enter the string you want to be replaced: ")
string_to_replace_with = input("Enter the string to replace with: ")

for filename in os.listdir(directory):
    file = os.path.join(directory, filename)
    if os.path.isfile(file):
        new_name = filename.replace(string_to_be_replaced, string_to_replace_with)
        new_file = '\\'.join((file.replace('/', '\\')).split('\\')[:-1]) + '\\' + new_name
        os.rename(file, new_file)