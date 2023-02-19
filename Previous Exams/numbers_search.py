def numbers_searching(*args):
    args = sorted(list(args))
    dupl = set()
    missing_num = None
    for i in range(len(args)-1):
        if args[i] == args[i+1]:
            dupl.add(args[i])
        elif args[i] == args[i+1]-1:
            continue
        elif args[i+1] - args[i] >= 2:
            for j in range(1, args[i+1] - args[i]):
                missing_num = args[i] + j
    result = [missing_num, sorted(list(dupl))]
    return result


print(numbers_searching(1, 2, 4, 2, 5, 4))
print(numbers_searching(5, 5, 9, 10, 7, 8, 7, 9))
print(numbers_searching(50, 50, 47, 47, 48, 45, 49, 44, 47, 45, 44, 44, 48, 44, 48))