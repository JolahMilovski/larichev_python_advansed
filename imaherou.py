from dataclasses import dataclass

@dataclass
class Hero:
    """
    Класс, представляющий героя с характеристиками и действиями.
    """
    #общий дамаг
    all_damage: int = 0

    #user's list
    users_list = []
    
    def __init__(self, name: str, hp: int, inventory_list: list, is_died: bool = False):
        """
        Конструктор героя.
        
        :param name: Имя героя
        :param hp: Максимальное здоровье (используется для установки)
        :param inventory_list: Начальный список инвентаря
        :param is_died: Статус жизни (по умолчанию False)
        """
        self.name = name
        self.hp = hp  
        self.inventory_list = inventory_list
        self.is_died = is_died
        Hero.users_list.append(self)
    
    def __eq__(self, value):
        """
        Одинаково ли HP героев
        """
        if not isinstance(value, Hero):
            return NotImplemented
        
        return self.hp == value.hp
    

    def __lt__(self, other):
        """
        Сравнивает героев по HP
        """
        if not isinstance(other, Hero):
            return NotImplemented
        return self.hp < other.hp
    

    def take_damage(self, dmg: int):
        """
        Наносит урон герою.
        
        :param dmg: Количество урона
        """
        Hero.all_damage += dmg
        self.hp -= dmg
        if self.hp <= 0:
            print("Hero is will be reborn")
            self.is_died = True

    def heal(self, healPoint: int):
        """
        Лечит героя, восстанавливая здоровье.
        
        :param healPoint: Количество восстанавливаемого здоровья
        """
        self.hp += healPoint
        print(f"{self.name} restored {healPoint} and now he has {self.hp}")

    def add_item(self, new_item: str):
        """
        Добавляет новый предмет в инвентарь героя.
        
        :param new_item: Название предмета
        """
        self.inventory_list.append(new_item)
        print(f'{self.name} find {new_item}')

    def show_status(self):
        """
        Выводит текущее состояние героя: имя, здоровье, статус жизни.
        """
        all_stats = []
        all_stats.append(self.name)
        all_stats.append(self.hp)
        all_stats.append(self.is_died)
        print(f"{all_stats}")

    @staticmethod
    def big_damage(dmg: int) -> int:
        """
        Статический метод для расчета усиленного урона.
        Не зависит от состояния объекта, является чистой утилитой.
        
        :param dmg: Базовый урон
        :return: Увеличенный урон (в 2 раза)
        """
        dmg = dmg*2
        Hero.all_damage += dmg

        # Увеличиваем урон в 2 раза, можно добавить любую другую логику
        return dmg

    @classmethod
    def show_all_damage(cls):
        """Классовый метод для расчета полного урона 
        нанесенного в бою"""
        print(f"all damage = {cls.all_damage}")

    @classmethod
    def total_user(cls):
        return len(cls.users_list)
    
    @classmethod
    def user_from_str(cls, data:str):
        name,hp,inventory_list,is_died = data.split(",")

        return cls(name, int(hp), inventory_list, is_died)

# Создаем героя с 120 HP
hero = Hero("NmF", 120, [], False)

# Добавляем предмет в инвентарь
hero.add_item("Флаг")

# Герой получает 25 урона
hero.take_damage(25)
hero.show_status()  # Должно быть: ["NmF", 95, False]

# Герой лечится на 15 HP
hero.heal(15)
hero.show_status()  # Должно быть: ["NmF", 110, False]

# Вызываем статический метод big_damage с аргументом 50
# Статик возвращает усиленный урон, который мы применяем к герою
damage_amount = Hero.big_damage(50)
print(f"Герой получает усиленный урон: {damage_amount}")

# Применяем усиленный урон к герою
hero.take_damage(damage_amount)
hero.show_status()  # Должно быть: ["NmF", 60, False]
hero.show_all_damage()

new_hero = Hero.user_from_str("Fedro,100,,0")
print(type(new_hero))
print(f"{new_hero.hp} {new_hero.is_died}")
print(hero == new_hero)
print(hero < new_hero)