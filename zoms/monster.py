import random

Weapons_for_zombies = ['HAMMER', 'KNIFE', 'POLL', 'CHAIN SAW', 'BITER']
BOSS_WEAPONS = ['SWORDS', 'CAR DOORS', 'RAY GUN', 'ROCKS']


class Zom:
    min_hit_points = 1
    max_hit_points = 1
    min_ex = 1
    max_ex = 1
    sound = 'YELLING'
    weapon = random.choice(Weapons_for_zombies)


    def __init__(self, **kwargs):
        self.hit_points = random.randint(self.min_hit_points, self.max_hit_points)
        self.ex = random.randint(self.min_ex, self.max_ex)
        self.weapon = random.choice(Weapons_for_zombies)

        for key, value in kwargs.items():
          setattr(self, key, value)

    def __str__(self):
        return 'Weapon: {} Type: {}, HP: {}, EX: {}'.format(self.weapon.title(),
                                              self.__class__.__name__,
                                              self.hit_points,
                                              self.ex)



class Small_zom(Zom):
    max_hit_points = 1
    max_ex = 1
    sound = 'GROWN'
    #weapon = random.choice(Weapons_for_zombies)


class Med_zom(Zom):
    max_hit_points = 2
    max_ex = 2
    sound = 'SCREEM'
    #weapon = random.choice(Weapons_for_zombies)


class Big_zom(Zom):
    max_hit_points = 4
    max_ex = 3
    sound = 'SCREEMING'
    #weapon = random.choice(Weapons_for_zombies)

class Big_boss_zom(Zom):
    max_hit_points = 8
    max_ex = 5
    sound = 'SCREEMING-ROARRRING'
    weapon = random.choice(BOSS_WEAPONS)
