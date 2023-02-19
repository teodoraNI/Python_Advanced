file = open("example.txt")
print(sum([int(line) for line in file]))
file.close()