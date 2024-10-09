class Animal:
    alive = True
    fed = False

    def __init__(self, name_of_animal):
        self.name_of_animal = name_of_animal


class Plant:
    edible = False

    def __init__(self, name_of_plant):
        self.name_of_plant = name_of_plant


class Mammal(Animal):  # МЛЕКОПИТАЮЩЕЕ

    def eat(self, food):
        if food != Flower:
            self.fed = True
            print(f'{self.name_of_animal} МЛЕКОПИТАЮЩЕЕ съело {food.name_of_plant}')
        else:
            self.alive = False
            print(f'{self.name_of_animal} МЛЕКОПИТАЮЩЕЕ НЕ ГЛУПОЕ, ОН НЕ БУДЕТ ЕСТЬ {food.name_of_plant}')


class Predator(Animal):  # ХИЩНИК

    def name(self):
        self.name = self.name_of_animal
        isinstance(self.name, str)
        return self.name

    def eat(self, food):

        if food != Flower:
            self.alive = False
            print(f'{self.name_of_animal} ХИЩНИК УМНЕЕ, ОН НЕ БУДЕТ ЕСТЬ {food.name_of_plant}')
        else:
            self.fed = True
            print(f'{self.name_of_animal} ХИЩНИК съел {food.name_of_plant}')


class Flower(Plant):  # РАСТЕНИЯ
    edible = False

    def name(self):
        self.name = self.name_of_plant
        isinstance(self.name, str)
        return self.name


class Fruit(Plant):  # ФРУКТЫ
    edible = True


a1 = Predator('Волк с Уолл-Стрит')
a2 = Mammal('Хатико')
p1 = Flower('Цветик семицветик')
p2 = Fruit('Заводной апельсин')

print(a1.name())
print(p1.name())
print(a1.alive)
print(a2.fed)
a1.eat(p1)
a2.eat(p2)
print(a1.alive)
print(a2.fed)
