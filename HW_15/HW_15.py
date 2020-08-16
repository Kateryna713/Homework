# Реализовать класс фигуры. На основе фигуры реализовать класс треугольника,
# квадрата и прямоугольника  с методами подсчета площади и периметра.
# Методы должны возвращать значение, а не принтить (это важно)

import math


class Figure:

    def __init__(self, side1):
        self.side1 = side1

    @property
    def side1(self):
        return self.__side1

    @side1.setter
    def side1(self, s1):
        if s1 > 0:
            self.__side1 = s1
        else:
            raise ValueError

    def area(self):
        pass

    def perimeter(self):
        pass

    def figInfo(self):
        s = self.area()
        p = self.perimeter()
        print(f'Perimetr =  {p}, Square = {s}')


class Rectangle(Figure):
    def __init__(self, side1, side2):
        self.side2 = side2
        super(Rectangle, self).__init__(side1)

    @property
    def side2(self):
        return self.__side2

    @side2.setter
    def side2(self, s2):
        if s2 > 0:
            self.__side2 = s2
        else:
            raise ValueError

    def area(self):
        area = self.side1 * self.side2
        return area

    def perimeter(self):
        perimeter = self.side1 * 2 + self.side2 * 2
        return perimeter


class Square(Figure):
    def __init__(self, side1):
        super(Square, self).__init__(side1)

    def perimeter(self):
        perimeter = 4 * self.side1
        return perimeter

    def area(self):
        area = self.side1 ** 2
        return area


class Triangle(Rectangle):
    def __init__(self, side1, side2, side3):
        self.side3 = side3
        super(Triangle, self).__init__(side1, side2)

    @property
    def side3(self):
        return self.__side3

    @side3.setter
    def side3(self, s3):
        if s3 > 0:
            self.__side3 = s3
        else:
            raise ValueError

    def perimeter(self):
        perimeter = self.side1 + self.side2 + self.side3
        return perimeter

    def area(self):
        p = (self.side1 + self.side2 + self.side3) / 2
        area = (p * (p - self.side1) * (p - self.side2) * (p - self.side3))
        return area


def main():
    choice = input("Rectangle(r), Triangle(t) or Square(s): ")
    if choice == 'r':
        side1 = float(input("Side 1: "))
        side2 = float(input("Side 2: "))
        r = Rectangle(side1, side2)
        r.figInfo()

    elif choice == 't':
        side1 = float(input("Side 1: "))
        side2 = float(input("Side 2: "))
        side3 = float(input("Side 3: "))
        t = Triangle(side1, side2, side3)
        t.figInfo()

    elif choice == 's':
        side1 = float(input("Side 1: "))
        s = Square(side1)
        s.figInfo()


if __name__ == '__main__':
    main()
