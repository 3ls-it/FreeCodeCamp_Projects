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
        return 2*self.width + 2*self.height

    def get_diagonal(self):
        return (self.width**2 + self.height**2)**.5

    def get_picture(self):
        if self.width > 50 or self.height > 50:
            return 'Too big for picture.'
        return ('\n'.join('*' * self.width for i in range(self.height)))+'\n'

    def get_amount_inside(self, other):
        if other.width > self.width or other.height > self.height:
            return 0
        elif other.width <= self.width and other.height <= self.height:
            nw = self.width // other.width
            nh = self.height // other.height
            return nw * nh


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
"""
r1 = Rectangle(4, 6)
print(r1)
print(f'Area: {r1.get_area()}')
print(f'Perimeter: {r1.get_perimeter()}')
print(f'Diagonal: {r1.get_diagonal()}')
print()
print(r1.get_picture())
print()

r1.set_width(4)
r1.set_height(3)
print(r1)
print(f'Area: {r1.get_area()}')
print(f'Perimeter: {r1.get_perimeter()}')
print(f'Diagonal: {r1.get_diagonal()}')
print()
print(r1.get_picture())
print()

s1 = Square(5)
print(s1)
print(f'Area: {s1.get_area()}')
print(f'Perimeter: {s1.get_perimeter()}')
print(f'Diagonal: {s1.get_diagonal()}')
print()
print(s1.get_picture())
print()

s2 = Square(51)
print(f'Area: {s2.get_area()}')
print(f'Perimeter: {s2.get_perimeter()}')
print(f'Diagonal: {s2.get_diagonal()}')
print()
print(s2.get_picture())
"""
