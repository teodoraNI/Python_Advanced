numbers = []
map_functions = {
    1: lambda x: numbers.append(x[1]),
    2: lambda x: numbers.pop() if numbers else None,
    3: lambda x: print(max(numbers)) if numbers else None,
    4: lambda x: print(min(numbers)) if numbers else None
}
for _ in range(int(input())):
    data = [int(x) for x in input().split()]
    map_functions[data[0]](data)
numbers.reverse()
print(*numbers, sep=', ')






# n = int(input())
# stack = []
# result = []
# for i in range(n):
#     command = input()
#     if command.startswith('1'):
#         stack.append(int(command.split()[1]))
#     elif command == '2':
#         if stack:
#             stack.pop()
#     elif command == '3':
#         if stack:
#             print(max(stack))
#     elif command == '4':
#         if stack:
#             print(min(stack))
# while stack:
#     result.append(str(stack.pop()))
# print(', '.join(result))
