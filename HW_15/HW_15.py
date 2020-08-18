class Figure:

    def __init__(self, side1):
        self.side1 = side1

    def square(self):
        raise NotImplementedError

    def perimeter(self):
        raise NotImplementedError

    def figInfo(self):
        s = self.square()
        p = self.perimeter()
        print(f'Perimetr =  {p}, Square = {s}')


class Square(Figure):
    def __init__(self, side1):
        super(Square, self).__init__(side1)

    def _validate_figure(self, side1):
        if side1 <= 0:
            raise ValueError

    def perimeter(self):
        perimeter = 4 * self.side1
        return perimeter

    def square(self):
        square = self.side1 ** 2
        return square


class Rectangle(Figure):
    def __init__(self, side1, side2):
        self.side2 = side2
        super().__init__(side1)

    def _validate_figure(self, side1, side2):
        if side1 <= 0:
            raise ValueError
        elif side2 <= 0:
            raise ValueError

    def square(self):
        square = self.side1 * self.side2
        return square

    def perimeter(self):
        perimeter = self.side1 * 2 + self.side2 * 2
        return perimeter


class Triangle(Figure):
    def __init__(self, side1, side2, side3):
        self.side2 = side2
        self.side3 = side3
        super().__init__(side1)

    def _validate_figure(self, side1, side2, side3):
        if side1 <= 0:
            raise ValueError
        elif side2 <= 0:
            raise ValueError
        if side3 <= 0:
            raise ValueError

    def perimeter(self):
        perimeter = self.side1 + self.side2 + self.side3
        return perimeter

    def square(self):
        p = (self.side1 + self.side2 + self.side3) / 2
        square = (p * (p - self.side1) * (p - self.side2) * (p - self.side3))
        return square


def main():
    choice = input("Rectangle(r), Triangle(t) or Square(s): ")
    if choice == 'r':
        side1 = float(input("Side 1: "))
        side2 = float(input("Side 2: "))
        r = Rectangle(side1, side2)
        r._validate_figure(side1, side2)
        r.figInfo()

    elif choice == 't':
        side1 = float(input("Side 1: "))
        side2 = float(input("Side 2: "))
        side3 = float(input("Side 3: "))
        t = Triangle(side1, side2, side3)
        t._validate_figure(side1, side2, side3)
        t.figInfo()

    elif choice == 's':
        side1 = float(input("Side 1: "))
        s = Square(side1)
        s._validate_figure(side1)
        s.figInfo()


if __name__ == '__main__':
    main()
