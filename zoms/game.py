import random

from monster import Small_zom
from monster import Med_zom
from monster import Big_zom
from monster import Big_boss_zom


team_z = [
Small_zom(),
Med_zom()
]

u = random.choice(team_z)
print(u)
