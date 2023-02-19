def even_odd(*args):
    command = args[-1]
    result = []
    for el in args[:-1]:
        if command == 'even' and int(el) % 2 == 0:
            result.append(el)
        elif command == 'odd' and int(el) % 2 == 1:
            result.append(el)
    return result

print(even_odd(1, 2, 3, 4, 5, 6, "even"))