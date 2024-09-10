class Rectangle:

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def get_square(self):
        return self.width * self.height

    def __eq__(self, other):
        return self.get_square() == other.get_square()

    def __add__(self, other):
        sum_area = self.get_square() + other.get_square()

        new_width = self.width

        new_height = sum_area // new_width

        while new_width * new_height != sum_area:
            new_width -= 1
            new_height = sum_area // new_width

        return Rectangle(new_width, new_height)

    def __mul__(self, n):
        new_area = self.get_square() * n

        return Rectangle(self.width, new_area // self.width)

    def __str__(self):
        return f"Rectangle(width={self.width}, height={self.height})"


r1 = Rectangle(25, 7)
r2 = Rectangle(23, 124)
assert r1.get_square() == 175, 'Test1'
assert r2.get_square() == 2852, 'Test2'

r3 = r1 + r2
assert r3.get_square() == 3027, 'Test3'

r4 = r3 * 4

assert r4.get_square() == 12108, 'Test4'

assert Rectangle(3, 6) == Rectangle(2, 9), 'Test5'
