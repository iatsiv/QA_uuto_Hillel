import math


class Figure:
    def perimeter(self):
        pass

    def area(self):
        pass


class Triangle(Figure):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def perimeter(self):
        return self.a + self.b + self.c

    def area(self):
        p = self.perimeter() / 2
        return math.sqrt(p * (p - self.a) * (p - self.b) * (p - self.c))


class Circle(Figure):
    def __init__(self, r):
        self.r = r

    def perimeter(self):
        return 2 * math.pi * self.r

    def area(self):
        return math.pi * (self.r ** 2)


class Rectangle(Figure):
    def __init__(self, w, h):
        self.w = w
        self.h = h

    def perimeter(self):
        return 2 * (self.w + self.h)

    def area(self):
        return self.w * self.h


class Square(Rectangle):
    def __init__(self, s):
        super().__init__(s, s)


t = Triangle(3, 4, 5)
print(t.perimeter())
print(t.area())

c = Circle(5)
print(c.perimeter())
print(c.area())

r = Rectangle(3, 4)
print(r.perimeter())
print(r.area())

s = Square(5)
print(s.perimeter())
print(s.area())
