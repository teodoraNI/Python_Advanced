nums = [int(x) for x in input().split()]
target_sum = int(input())

targets = set()
values_map = {}

for value in nums:
    if value in targets:
        targets.remove(value)
        pair = values_map[value]
        print(f'{pair} + {value} = {target_sum}')
        del values_map[value]
    else:
        result = target_sum - value
        targets.add(result)
        values_map[result] = value

