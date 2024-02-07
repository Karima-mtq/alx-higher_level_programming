#!/usr/bin/python3
"""
write file
"""

def write_file(filename=""):
    """ write file"""
    with open(filename, "w", encoding="UTF-8") as f:
        print(f.read(), end="")
