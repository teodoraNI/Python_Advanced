symbols = ["-", ",", ".", "!", "?"]
with open("text.txt", "r") as lines:
    text  = lines.readlines()
for i in range(0, len(text), 2):
    for symbol in symbols:
        text[i] = text[i].replace(symbol, "@")
    print(*text[i].split()[::-1])