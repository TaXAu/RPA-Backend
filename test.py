a = tuple[int, str]
c: a = (1, "s")
b = a.__args__
print(isinstance(c, tuple))
