#!/data/data/com.termux/files/usr/bin/env python3

class Rectangle:

    def __init__(self, width, height):
        self.width = width
        self.height = height
  
    def __str__(self):
        return f'Rectangle(width={self.width}, height={self.height})'

    def set_width(self, w):
        self.width = w

    def set_height(self, h):
        self.height = h

    def get_area(self):
        return self.width * self.height

    def get_perimeter(self):
        return 2 * self.width + 2 * self.height

    def get_diagonal(self):
        return (self.width**2 + self.height**2)**.5

    def get_picture(self):
        """
        Returns a string that represents the shape using lines of '*'. The number of lines should be equal to the height and the number of '*' in each line should be equal to the width. There should be a new line (\n) at the end of each line. If the width or height is larger than 50, this should return the string: 'Too big for picture.'.
        """
        pass

    def get_amount_inside(self):
        """
        Takes another shape (square or rectangle) as an argument. Returns the number of times the passed in shape could fit inside the shape (with no rotations). For instance, a rectangle with a width of 4 and a height of 8 could fit in two squares with sides of 4.
        """
        pass


class Square(Rectangle):

    def __init__(self, side):
        super().__init__(side, side)
        self.side = side
        self.width = self.side
        self.height = self.side

    def __str__(self):
        return f'Square(side={self.side})'

    def set_side(self, s):
        self.side = s
        self.width = self.side
        self.height = self.side

    def set_width(self, w):
        self.set_side(w)

    def set_height(self, h):
        self.set_side(h)

## Tests
r1 = Rectangle(4, 6)
print(r1)
print(f'Area: {r1.get_area()}')
print(f'Perimeter: {r1.get_perimeter()}')
print(f'Diagonal: {r1.get_diagonal()}')
print()

r1.set_width(4)
r1.set_height(3)
print(r1)
print(f'Area: {r1.get_area()}')
print(f'Perimeter: {r1.get_perimeter()}')
print(f'Diagonal: {r1.get_diagonal()}')
print()

s1 = Square(5)
print(s1)
print(f'Area: {s1.get_area()}')
print(f'Perimeter: {s1.get_perimeter()}')
print(f'Diagonal: {s1.get_diagonal()}')
print()



"""
Rectangle class

When a Rectangle object is created, it should be initialized with width and height attributes. The class should also contain the following methods:


get_picture: Returns a string that represents the shape using lines of '*'. The number of lines should be equal to the height and the number of '*' in each line should be equal to the width. There should be a new line (\n) at the end of each line. If the width or height is larger than 50, this should return the string: 'Too big for picture.'.

get_amount_inside: Takes another shape (square or rectangle) as an argument. Returns the number of times the passed in shape could fit inside the shape (with no rotations). For instance, a rectangle with a width of 4 and a height of 8 could fit in two squares with sides of 4.

Additionally, if an instance of a Rectangle is represented as a string, it should look like: 'Rectangle(width=5, height=10)'.


Square class

The Square class should be a subclass of Rectangle. When a Square object is created, a single side length is passed in. The __init__ method should store the side length in both the width and height attributes from the Rectangle class.

The Square class should be able to access the Rectangle class methods but should also contain a set_side method. If an instance of a Square is represented as a string, it should look like: 'Square(side=9)'.

Additionally, the set_width and set_height methods on the Square class should set both the width and height.
"""
