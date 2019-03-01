""" In this mission your task is to add new classes and functions to the existing ones.
The new class should be the Army and have the method add_units() - for adding the chosen amount of units to the army.
Also you need to create a Battle() class with a fight() function, which will determine the strongest army.
The battles occur according to the following principles:
at first, there is a duel between the first warrior of the first army and the first warrior of the second army.
As soon as one of them dies - the next warrior from the army that lost the fighter enters the duel, and the surviving
warrior continues to fight with his current health. This continues until all the soldiers of one of the armies die.
In this case, the battle() function should return True, if the first army won, or False, if the second one was stronger.
"""


class Warrior:
    def __init__(self):
        self.health = 50
        self.attack = 5

    @property
    def is_alive(self):
        return self.health > 0

    def hit(self, other_warrior):
        """ The hit warrior loses as much health as is the hitting warrior's attack power."""
        other_warrior.health -= self.attack


class Knight(Warrior):
    def __init__(self):
        super().__init__()
        self.attack = 7


def fight(first_warrior, second_warrior):
    while first_warrior.is_alive and second_warrior.is_alive:
        first_warrior.hit(second_warrior)
        # The second warrior hits only if still alive:
        if second_warrior.is_alive:
            second_warrior.hit(first_warrior)
    else:
        if first_warrior.is_alive:
            return True
        return False


class Army:
    def __init__(self):
        self.army_lst = []

    def add_units(self, unit_type, number):
        """Add chosen number of units to the army.
        :param unit_type: object - the type of soldier to add to the army: Warrior or Knight
        :param number: int - the number of soldiers of a given type to be added to the army list
        """
        if unit_type is Warrior:
            for _ in range(number):
                self.army_lst.append(Warrior())  # This way we are creating different objects, not the same one!
        else:
            for _ in range(number):
                self.army_lst.append(Knight())
        # return self.army_lst

    def __iter__(self):
        """ Iterate through the army list"""
        yield from self.army_lst

    def __len__(self):
        """ Define the length of the army as the length of the army list."""
        return len(self.army_lst)


class Battle:
    def __init__(self):
        pass

    @staticmethod
    def fight(first_army, second_army):
        while len(first_army) > 0 and len(second_army) > 0:
            first_warrior_won = fight(first_army.army_lst[0], second_army.army_lst[0])
            if first_warrior_won:
                second_army.army_lst.remove(second_army.army_lst[0])
            else:
                first_army.army_lst.remove(first_army.army_lst[0])
        if len(first_army) > 0:
            return True
        return False


# Examples:
chuck = Warrior()
bruce = Warrior()
carl = Knight()
dave = Warrior()
mark = Warrior()

print(fight(chuck, bruce))  # == True
print(fight(dave, carl))  # == False
print(chuck.is_alive)  # == True
print(bruce.is_alive)  # == False
print(carl.is_alive)  # == True
print(dave.is_alive)  # == False
print(fight(carl, mark))  # == False
print(carl.is_alive)  # == False

print('--------------------------------')
my_army = Army()
my_army.add_units(Knight, 3)

enemy_army = Army()
enemy_army.add_units(Warrior, 3)

army_3 = Army()
army_3.add_units(Warrior, 20)
army_3.add_units(Knight, 5)
# print(army_3)

army_4 = Army()
army_4.add_units(Warrior, 30)

battle = Battle()

print('battle fight:', battle.fight(my_army, enemy_army))  # == True
print('battle fight (must be False):', battle.fight(army_3, army_4))  # == False

army_1 = Army()
army_2 = Army()
army_1.add_units(Warrior, 20)
army_2.add_units(Warrior, 21)
battle = Battle()
print('battle fight:', battle.fight(army_1, army_2))  # True
