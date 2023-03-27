foo = ["Hello", "Howdy", "Hi"]

print(foo.index("Howdy"))

if "Goodbye" in foo:
    print(foo.index("Goodbye"))
else:
    print("Cannot find Goodbye")

try:
    print(foo.index("Goodbye"))
except ValueError:
    print("Cannot find Goodbye")
