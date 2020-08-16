class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.__friends = []

    def is_known(self, person):
        if person in self.__friends:
            return True
        return False

    def know(self, person):
        if self.is_known(person):
            print(f'{self.name} knows {person.name}')

        else:
            print(f'{self.name} doesn\'t know {person.name}')
            self.__friends.append(person)

            print(f'{person.name} is added to {self.name}\'s friends list.')


def main():
    P = Person('Anna', 25)

    person1 = Person('Dima', 30)
    person2 = Person('Oleg', 35)
    person3 = Person('Yulya', 27)
    person4 = Person('Tanya', 20)

    P.know(person1)
    P.know(person4)
    P.know(person2)
    P.know(person1)


if __name__ == '__main__':
    main()
