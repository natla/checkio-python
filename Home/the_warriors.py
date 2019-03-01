""" You need to create the class Warrior, the instances of which will have 2 parameters - health (equal to 50 points)
and attack (equal to 5 points), and 1 property - is_alive, which can be True (if warrior's health is > 0) or False
(in the other case). In addition you have to create the second unit type - Knight, which should be the subclass of
the Warrior but have the increased attack - 7. Also you have to create a function fight(), which will initiate the duel
between 2 warriors and define the strongest of them. The duel occurs according to the following principle:
every turn one of the warriors will hit another one and the last will lose his health in the same value as the attack
of the first warrior. After that, the second warrior will do the same to the first one.
If in the end of the turn the first warrior has > 0 health and the other one doesn’t, the function should return True,
in the other case it should return False.
"""


class Warrior:
    def __init__(self):
        self.health = 50
        self.attack = 5

    @property
    def is_alive(self):
        return self.health > 0

    def hit(self, other_warrior):
        other_warrior.health -= self.attack


class Knight(Warrior):
    def __init__(self):
        super().__init__()
        self.attack = 7


def fight(first_warrior, second_warrior):
    while first_warrior.is_alive and second_warrior.is_alive:
        first_warrior.hit(second_warrior)
        if second_warrior.is_alive:
            second_warrior.hit(first_warrior)
            #print(second_warrior.is_alive)
    else:
        if first_warrior.is_alive and not second_warrior.is_alive:
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
