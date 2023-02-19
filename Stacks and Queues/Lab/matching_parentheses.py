data = input()
indexes = []
for i in range(len(data)):
    if data[i] == '(':
        indexes.append(i)
    elif data[i] == ')':
        x = indexes.pop()
        print(data[x: i+1])

