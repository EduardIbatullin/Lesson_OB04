# Домашнее задание к уроку № OB04. Принципы SOLID.

# Задание: Применение Принципа Открытости/Закрытости (Open/Closed Principle) в Разработке Простой Игры.#
# Цель: Цель этого домашнего задание - закрепить понимание и навыки применения принципа открытости/закрытости
# (Open/Closed Principle), одного из пяти SOLID принципов объектно-ориентированного программирования.
# Принцип гласит, что программные сущности (классы, модули, функции и т.д.) должны быть открыты для расширения,
# но закрыты для модификации.
# # Задача: Разработать простую игру, где игрок может использовать различные типы оружия для борьбы с монстрами.
# Программа должна быть спроектирована таким образом, чтобы легко можно было добавлять новые типы оружия, не изменяя
# существующий код бойцов или механизм боя.

from abc import ABC, abstractmethod


class Weapon(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def attack(self):
        pass


class Sword(Weapon):
    def __init__(self):
        super().__init__("меч")

    def attack(self):
        print("Боец наносит удар мечём.")


class Bow(Weapon):
    def __init__(self):
        super().__init__("лук")

    def attack(self):
        print("Боец стреляет из лука.")


class Axe(Weapon):
    def __init__(self):
        super().__init__("топор")

    def attack(self):
        print("Боец наносит удар топором.")


class Fighter:
    def __init__(self, weapon: Weapon):
        self.weapon = weapon

    def change_weapon(self, new_weapon):
        self.weapon = new_weapon
        print(f"\nБоец выбирает в качестве оружия - {new_weapon.name}")

    def attack(self):
        self.weapon.attack()


class Monster:
    def dead_monster(self):
        print(f"Монстр умирает.")


fighter = Fighter(None)
monster = Monster()

sword = Sword()
bow = Bow()
axe = Axe()

fighter.change_weapon(bow)
fighter.attack()
monster.dead_monster()

fighter.change_weapon(axe)
fighter.attack()
monster.dead_monster()

fighter.change_weapon(sword)
fighter.attack()
monster.dead_monster()
