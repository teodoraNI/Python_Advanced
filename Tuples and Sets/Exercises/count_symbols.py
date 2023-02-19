result = {}
for symbol in input():
    if symbol not in result:
        result[symbol] = 0
    result[symbol] += 1
[print(f'{key}: {value} time/s') for key, value in sorted(result.items())]