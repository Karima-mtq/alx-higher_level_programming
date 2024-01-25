#!/usr/bin/python3
def add_integer(a, b=98):
    if not isinstance(a, int) and not isinstance(a, float):
        print("a must be an integer")
    if not isinstance(b, int) and not isinstance(b, float):
        print("b must be an integer")
    return int(a) + int(b)

if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/0-add_integers.txt")
