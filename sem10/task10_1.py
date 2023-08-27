"""
Создайте класс-фабрику.
Класс принимает тип животного (название одного из созданных классов)
и параметры для этого типа.
Внутри класса создайте экземпляр на основе переданного типа и верните
его из класса-фабрики
"""

class Animal:
    def __init__(self, kind, name, age):
        self._kind = kind
        self._name = name
        self._age = age

    def get_kind(self):
        return self._kind

    def get_name(self):
        return self._name

    def get_age(self):
        return self._age

    def up_age(self):
        self._age += 1

    def get_animal_info(self):
        return f'Вид: {self.get_kind()}, кличка: {self.get_name()}, возраст: {self.get_age()} лет,' \
               f' special: {self.get_specific()}'

class Alligator(Animal):

    def __init__(self, kind, name, age, size):
        super().__init__(kind, name, age)
        self._size = size

    def get_specific(self):
        return self._size

class Dog(Animal):

    def __init__(self, kind, name, age, color):
        super().__init__(kind, name, age)
        self._color = color

    def get_specific(self):
        return self._color

class Cat(Animal):

    def __init__(self, kind, name, age, spec):
        super().__init__(kind, name, age)
        self._spec = spec

    def get_specific(self):
        return self._spec

class Factory:

    def create_animal(self, kind, name, age, spec):
        if kind.lower() == "alligator":
            return Alligator(kind, name, age, spec)
        elif kind.lower() == "dog":
            return Dog(kind, name, age, spec)
        elif kind.lower() == "cat":
            return Cat(kind, name, age, spec)
        else:
            raise ValueError("Данный тип отсутствует.")

factory = Factory()

alligator = factory.create_animal("alligator", "Саймон", 10, "длинный")
dog = factory.create_animal("dog", "Терминатор", 10, "агрессивный")
cat = factory.create_animal("cat", "Васька", 11, "усатый")

print(alligator.get_animal_info())
print(dog.get_animal_info())
print(cat.get_animal_info())