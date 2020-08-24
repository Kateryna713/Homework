"""
Нужно дописать основную линию сказки. Каждого героя реализовать классом с методами.
Так же должен быть класс сказки (или функция), где происходит основное действие с героями
"""


# ___________KOLOBOK_______________
from typing import List


class Hero:

    def __init__(self, name):
        self.name = name


class Animal(Hero):

    def __init__(self, name):
        super().__init__(name)

    def __str__(self):
        return self.name

    def says(self,colobok):
        print(f' {self.name} says: "{colobok.name}, {colobok.name}, I want to eat you!" ')


class Colobok(Hero):

    def __init__(self, name):
        super().__init__(name)

    def runs(self):
        print(f" {self.name} runs away.")

    def meet(self, animal):
        print(f" {self.name} meets a {animal}.")

    def sing_the_song(self, animal):
        print(f' {self.name} sing : "I ran away from all, and I can run away from you,{animal}." ')

    def jumps_on_the_nose(self,fox):
        print(f' {self.name} jumps on the {fox.name} nose.')


class Babka(Hero):

    def __init__(self, name):
        super().__init__(name)

    def bake_colobok(self, colobok):
        print(f' {self.name} bake {colobok.name}.')


class Ded(Hero):

    def __init__(self, name):
        super().__init__(name)

    def ask_to_babka_about_colobok(self, babka):
        print(f' Ded said: {babka.name}, please, bake me a bun!')


class Fox(Hero):
    def __init__(self, name):
        super().__init__(name)

    def called_out(self, colobok):
        print(f' {self.name} called out {colobok.name}: "I cannot hear you well. Sit on my nose and sing your song again." ')

    def eats_colobok(self, colobok):
        print(f' {self.name} eats {colobok.name}(( ')


class Tale:

    def __init__(self, babka, ded, colobok, fox, animals):
        self.babka = babka
        self.ded = ded
        self.colobok = colobok
        self.animals = animals
        self.fox = fox

    def babkin_dom(self):
        self.ded.ask_to_babka_about_colobok(self.babka)
        self.babka.bake_colobok(self.colobok)

    def colobok_road(self):
        self.colobok.runs()
        for animal in self.animals:
            self.colobok.meet(animal)
            animal.says(self.colobok)
            self.colobok.sing_the_song(animal)
            self.colobok.runs()
        self.fox.called_out(self.colobok)
        self.colobok.jumps_on_the_nose(self.fox)
        self.fox.eats_colobok(self.colobok)

    def start(self):
        self.babkin_dom()
        self.colobok_road()


B = Babka('Babka')
D = Ded('Ded')
C = Colobok('Colobok')
H = Animal('Hare')
W = Animal('Wolf')
Be = Animal('Bear')
Fo = Animal('Fox')
F = Fox('Fox')
A = [H, W, Be, Fo]

my_tail = Tale(B, D, C, F, A)
my_tail.start()

