import pygame
import sys
from Entity import Entity
from abc import ABC, abstractmethod

class Character(Entity, ABC):
    
    @abstractmethod
    def __init__(self, character_name, base_health, base_physical, base_magic, base_phys_resist, base_mag_resist, companion):
        super().__init__()
        self.name = character_name
        self.health = base_health
        self.physical = base_physical
        self.magic = base_magic
        self.phys_resist = base_phys_resist
        self.mag_resist = base_mag_resist
        self.companion = companion #To be replaced with companion object
        self.abilities = []

    @abstractmethod
    def update(self):
        pass

    @abstractmethod
    def draw(self):
        pass