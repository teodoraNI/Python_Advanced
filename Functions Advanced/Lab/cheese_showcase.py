def sorting_cheeses(**kwargs):
    sorted_cheese = sorted(kwargs.items(), key=lambda x: (-len(x[1]), x[0]))
    result = []
    for key, value in sorted_cheese:
        result.append(key)
        quantity_list  = sorted(value, reverse = True)
        result += quantity_list
    return '\n'.join([str(x) for x in result])

print(sorting_cheeses(Parmesan=[102, 120, 135], Camembert=[100, 100, 105, 500, 430], Mozzarella=[50, 125],))