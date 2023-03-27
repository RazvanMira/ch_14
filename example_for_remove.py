foo = [10, 13, 24, 36, 38, 48]
print(foo)

foo.remove(36)
print(foo)

del foo[foo.index(13)]
print(foo)