class Number:
    def __init__(self, n):
        self.realNumber = n

class ComplexNumber(Number):
    def __init__(self, re, im):
        Number.__init__(self, re)
        self.imaginaryNumber = im

    def complex_number(self):
        return (self.realNumber, self.imaginaryNumber)


n1 = Number(4)
n2 = ComplexNumber(2, 5)

print(n2.realNumber)
print(n2.imaginaryNumber)