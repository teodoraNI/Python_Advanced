# set1 = set(int(x) for x in input().split())
# set2 = set(int(x) for x in input().split())
#
# for _ in range(int(input())):
#     action, *data = input().split()
#     command = action + ' ' + data.pop(0)
#     if command == 'Add First':
#         [set1.add(int(num)) for num in data]
#     elif command == 'Add Second':
#         [set2.add(int(num)) for num in data]
#     elif command == 'Remove First':
#         [set1.discard(int(num)) for num in data]
#     elif command == 'Remove Second':
#         [set2.discard(int(num)) for num in data]
#     else:
#         print(set1.issubset(set2) or set2.issubset(set1))
# print(*sorted(set1), sep=', ')
# print(*sorted(set2), sep=', ')


set1 = set(int(x) for x in input().split())
set2 = set(int(x) for x in input().split())

functions = {
    "Add First": lambda x: [set1.add(int(el)) for el in x],
    "Add Second": lambda x: [set2.add(int(el)) for el in x],
    "Remove First": lambda x: [set1.discard(int(el)) for el in x],
    "Remove Second": lambda x: [set2.discard(int(el)) for el in x],
    "Check Subset": lambda: print(set1.issubset(set2) or set2.issubset(set1))
}
for _ in range(int(input())):
    action, *data = input().split()
    command = action + ' ' + data.pop(0)
    if data:
        functions[command](data)
    else:
        functions[command]()
print(*sorted(set1), sep=', ')
print(*sorted(set2), sep=', ')

