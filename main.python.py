from abc import ABC, abstractmethod
import random


# Шаг 1: Создаем абстрактный класс для оружия
class Weapon(ABC):
    @abstractmethod
    def attack(self) -> str:
        pass


# Шаг 2: Реализуем конкретные типы оружия
class Sword(Weapon):
    def attack(self) -> str:
        return "Боец наносит удар мечом."


class Bow(Weapon):
    def attack(self) -> str:
        return "Боец стреляет из лука."


# Шаг 3: Модифицируем класс Fighter
class Fighter:
    def __init__(self, name: str, weapon: Weapon):
        self.name = name
        self.weapon = weapon

    def change_weapon(self, weapon: Weapon):
        self.weapon = weapon
        print(f"{self.name} меняет оружие.")

    def attack_monster(self, monster: 'Monster'):
        print(self.weapon.attack())
        if random.choice([True, False]):  # случайный шанс победы
            print("Монстр побежден!")
        else:
            print("Монстр выжил!")


# Класс Monster
class Monster:
    def __init__(self, name: str):
        self.name = name


# Шаг 4: Реализация боя
def main():
    # Создаем бойца и монстра
    fighter = Fighter("Боец", Sword())
    monster = Monster("Монстр")

    # Боец атакует монстра с мечом
    print(f"{fighter.name} выбирает меч.")
    fighter.attack_monster(monster)

    # Боец меняет оружие на лук
    fighter.change_weapon(Bow())

    # Боец атакует монстра с луком
    print(f"{fighter.name} выбирает лук.")
    fighter.attack_monster(monster)


if __name__ == "__main__":
    main()