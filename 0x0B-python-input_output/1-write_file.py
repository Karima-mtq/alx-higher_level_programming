#!/usr/bin/python3
"""
write file mod
"""

def write_file(filename="", text=""):
    """def write file"""
    with open(filename, "w", encoding="UTF-8") as f:
        return f.write(text)
