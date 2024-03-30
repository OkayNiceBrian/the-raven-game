import pygame
import sys
from Ability import Ability
import util.AbilityTypes as AbilityTypes
from Entity import Entity
from abc import ABC, abstractmethod

class BoneShot(Ability):

    def __init__(self, base_damage=100):
        super().__init__(name="Bone Shot", 
                        type=AbilityTypes.skillshot,
                        description="Shoots a magic bone at your opponent.",
                        level=0)
        self.base_damage = base_damage

    def effect(self, Game, playerCharacter, opponentCharacter):
        damageDealt = self.base_damage * self.level
        damageDealt = damageDealt - opponentCharacter.mag_resist

    def update(self):
        pass

    def draw(self):
        pass