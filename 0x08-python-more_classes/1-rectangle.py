#!/usr/bin/python3
"""Defines a class Rectangle"""


class Rectangle:
    """Represents a Rectangle"""
    def __init__(self, width=0, height=0):
        """Initializes a new square

        Args:
            width(int): Width of the new rectangle
            height(int): Height of the new rectangle.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Get the width of the current rectangle"""
        return (self.__width)

    @width.setter
    def width(self, value):
        """Set the width of the current rectangle"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        # set the value otherwise
        self.__width = value

    @property
    def height(self):
        """Get the height of the current rectangle"""
        return (self.__height)

    @height.setter
    def height(self, value):
        """Set the height of the current rectangle"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        # set the value otherwise
        self.__height = value
