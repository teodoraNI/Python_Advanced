import re

result = {}
with open('words.txt', 'r') as file:
    words = (file.read()).split()
selection = []
with open('text.txt', 'r') as file:
    text = file.read()
    selection = [x.lower() for x in re.findall(r'[a-zA-Z]+', text)]
    for word in words:
        result[word] = selection.count(word)
[print(f'{key} - {value}') for key, value in sorted(result.items(), key=lambda x: x[1], reverse=True)]




