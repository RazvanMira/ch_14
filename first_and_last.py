# first_last(foo: list | str)
# first_last([1, 2, 3, 4]) -> [1, 4]
# first_last("abcd") -> "ad"


def first_last(array):
    first = array[:1] # if we slice a list we get a list
    last = array[-1:] # if we slice a string we get a string
    result = first + last
    return result

def main() -> None:
    test_list = [1, 2, 3, 4]
    test_str = "abcd"
    assert [1, 4] == first_last(test_list)
    assert "ad" == first_last(test_str)
    print("Everything went fine!")

if __name__ == "__main__":
    main()