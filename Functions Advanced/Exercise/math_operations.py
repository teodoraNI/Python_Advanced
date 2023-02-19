def math_operations(*args, **kwargs):
    for i in range(0, len(args), +4):
        kwargs['a'] += args[i]
        if i+1 < len(args):
            kwargs['s'] -= args[i+1]
        if i +2 < len(args) and args[i+2] != 0:
            kwargs['d'] /= args[i+2]
        if i +3 < len(args):
            kwargs['m'] *= args[i+3]
    result = [f"{key}: {value:.1f}" for key, value in sorted(kwargs.items(), key=lambda x: (-x[1], x[0]))]
    return '\n'.join(result)

print(math_operations(2.1, 12.56, 0.0, -3.899, 6.0, -20.65, a=1, s=7, d=33, m=15))
# d: 33.0 s: 15.1 a: 9.1 m: -58.5
