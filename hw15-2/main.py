class Fraction:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __mul__(self, other):
        numerator = self.a * other.a
        denominator = self.b * other.b

        return Fraction(numerator, denominator)

    def __add__(self, other):

        denominator = self.b * other.b

        new_numerator1 = self.a * other.b
        new_numerator2 = other.a * self.b

        result_numerator = new_numerator1 + new_numerator2

        return Fraction(result_numerator, denominator)

    def __sub__(self, other):

        denominator = self.b * other.b

        new_numerator1 = self.a * other.b
        new_numerator2 = other.a * self.b

        result_numerator = new_numerator1 - new_numerator2

        return Fraction(result_numerator, denominator)

    def __eq__(self, other):
        denominator = self.b * other.b

        new_numerator1 = self.a * other.b
        new_numerator2 = other.a * self.b

        return new_numerator1 == new_numerator2

    def __gt__(self, other):

        denominator = self.b * other.b

        new_numerator1 = self.a * other.b
        new_numerator2 = other.a * self.b

        return new_numerator1 > new_numerator2

    def __lt__(self, other):
        denominator = self.b * other.b

        new_numerator1 = self.a * other.b
        new_numerator2 = other.a * self.b

        return new_numerator1 < new_numerator2

    def __str__(self):
        return f"Fraction: {self.a}, {self.b}"


f_a = Fraction(2, 3)
f_b = Fraction(3, 6)
f_c = f_b + f_a

assert str(f_c) == 'Fraction: 21, 18'
f_d = f_b * f_a
assert str(f_d) == 'Fraction: 6, 18'
f_e = f_a - f_b
print(f_e)
assert str(f_e) == 'Fraction: 3, 18'

assert f_d < f_c  # True
assert f_d > f_e  # True
assert f_a != f_b  # True
f_1 = Fraction(2, 4)
f_2 = Fraction(3, 6)
assert f_1 == f_2  # True
print('OK')
