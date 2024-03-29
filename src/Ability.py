import pygame
import sys
from Entity import Entity
from abc import ABC, abstractmethod

class Ability(Entity, ABC):
    
    @abstractmethod
    def __init__(self, name, type, description, level):
        super().__init__()
        self.name = name
        self.type = type
        self.description = description
        self.level = level

    @abstractmethod
    def effect(self):
        pass

    def levelUp(self):
        self.level = self.level + 1

    def levelDown(self):
        if (self.level > 0):
            self.level = self.level - 1

    @abstractmethod
    def update(self):
        pass

    @abstractmethod
    def draw(self):
        pass