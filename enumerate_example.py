foo = [10, 13, 24, 36, 38, 48]

i = 0
for number in foo:
    print(number * 1)
    i = i + 1

    for index, number in enumerate(foo):
        print(number * (index + 1))