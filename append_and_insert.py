foo = [10, 13, 24, 36, 38, 48]
print(foo)

foo.append(59)
print(foo)

foo.insert(3, 64)
print(foo)

foo.extend([11, 12])
print(foo)

foo[4:4] = [71, 72]
print(foo)