import random
import os

class Ability():
    def __init__(self, name, max_damage):
        self.name = name 
        self.max_damage = max_damage 
    def attack(self)