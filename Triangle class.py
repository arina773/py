class Triangle:
    
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def perimeter(self):
        return self.a + self.b +self.c

    def area(self):
        p = (self.a + self.b +self.c) / 2
        return (p * (p - self.a) * (p - self.b) * (p - self.c)) ** 0.5

    def scale(self, scale_f):
        return Triangle(scale_f * self.a, scale_f * self.b, scale_f * self.c)

    def is_valid(self):
        if self.a + self.b > self.c and self.a + self.c > self.b and self.c + self.b > self.a:
            return True
        return False

    def is_right(self):
        if self.a ** 2 + self.b ** 2 == self.c ** 2:
            return True
        elif self.a ** 2 + self.c ** 2 == self.b ** 2:
            return True
        elif self.b ** 2 + self.c ** 2 == self.a ** 2:
            return True
        return False
    
