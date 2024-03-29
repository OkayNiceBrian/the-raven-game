import pygame
import sys
from Entity import Entity
from abc import ABC, abstractmethod

class Player(Entity, ABC):
    
    @abstractmethod
    def __init__(self):
        super().__init__()

    @abstractmethod
    def update(self):
        pass

    @abstractmethod
    def draw(self):
        pass