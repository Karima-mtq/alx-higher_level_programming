#!/usr/bin/python3
# 0-rectangle.py
# By karima
"""Defines class: Rectangle."""


class Rectangle:
    """Represent rectangle."""

    def __init__(self, width = 0, height = 0):
        """initialize

        Args:
            width (int)
            height (int)
        """
        self.__height = height
        self.__width = width

        @property
        def height(self):
            """get or set the height"""
            return self.__height

        @height.setter
        def height(self, value):
            if not isinstance(value, int):
                raise TypeError("height must be an integer")
            if value < 0:
                raise TypeError("height must be >= 0")
            self.__height = value

        @property
        def width(self):
            """get or set the width"""
            return self.__width

        @width.setter
        def width(self, value):
            if not isinstance(value, int):
                raise TypeError("width must be an integer")
            if value < 0:
                raise TypeError("width must be >= 0")
            self.__width = value
