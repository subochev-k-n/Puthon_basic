class Complex:

    def __init__(self, a=0, b=0):
        self.a = a
        self.b = b

    def __add__(self, other):
        return Complex(self.a + other.a, self.b + other.b)

    def __mul__(self, other):
        return Complex(self.a * other.a - self.b * other.b, self.a * other.a + self.b * other.b)

    def __str__(self):
        if self.b >= 0:
            return f"{self.a} + i*{self.b}"
        else:
            return f"{self.a} - i*{abs(self.b)}"


m1 = Complex(5, 7)
m2 = Complex(4, -4)

print(m1)
print(m2)

print(m1 + m2)
print(m1 * m2)
