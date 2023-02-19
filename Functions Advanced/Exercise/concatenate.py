def concatenate(*args, **kwargs):
    expr = ''.join(args)
    for key in kwargs:
        expr = expr.replace(key, kwargs[key])
    return expr



print(concatenate("Soft", "UNI", "Is", "Grate", "!", UNI="Uni", Grate="Great"))
print(concatenate("I", " ", "Love", " ", "Cythons", C="P", s="", java='Java'))