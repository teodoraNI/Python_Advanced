import os

def save_extentions(dir_path, first_level = False):
    for filename in os.listdir(dir_path):
        file = os.path.join(dir_path, filename)
        if os.path.isfile(file):
            extention = filename.split('.')[-1]
            if extention not in extentions:
                extentions[extention] = []
            extentions[extention].append(filename)
        elif os.path.isdir(file) and not first_level:
            save_extentions(file, first_level = True)



directory = input()
extentions = {}
result = []

save_extentions(directory)
extentions = sorted(extentions.items(), key=lambda x: x[0])
for extention, files in extentions:
    result.append(f'{extention}')
    for file in sorted(files):
        result.append(f'- - -{file}')
with open('report.txt', 'w') as file:
    file.write('\n'.join(result))


