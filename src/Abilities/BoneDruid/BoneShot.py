import pygame
import sys
import util.AbilityTypes as AbilityTypes
from Entity import Entity
from abc import ABC, abstractmethod

class BoneShot():

    def __init__(self):
        super().__init__(name="Bone Shot", 
                        type=AbilityTypes.skillshot,
                        description="Shoots a magic bone at your opponent.")

    @abstractmethod
    def effect(self):
        pass

    @abstractmethod
    def update(self):
        pass

    @abstractmethod
    def draw(self):
        pass