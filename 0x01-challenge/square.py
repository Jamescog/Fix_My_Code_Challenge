#!/usr/bin/python3
"""
This script contains fixed code for task 1
"""


class Square():
    """Defines the class square
    """

    width = 0
    height = 0

    def __init__(self, *args, **kwargs):
        """Initialize the class with key word arguments
        """
        for key, value in kwargs.items():
            setattr(self, key, value)

    def area_of_my_square(self):
        """ Area of the square """
        return self.height * self.width

    def PermiterOfMySquare(self):
        """Computes the parameter of the square
        """
        return (self.width * 2) + (self.height * 2)

    def __str__(self):
        return "{}/{}".format(self.width, self.height)


if __name__ == "__main__":

    s = Square(width=12, height=9)
    print(s)
    print(s.area_of_my_square())
    print(s.PermiterOfMySquare())
