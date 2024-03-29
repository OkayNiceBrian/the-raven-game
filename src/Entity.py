import pygame
import sys
from abc import ABC, abstractmethod

class Entity(ABC):
    
    @abstractmethod
    def __init__(self): 
        self.x = 0
        self.y = 0

    @abstractmethod
    def update(self):
        pass

    @abstractmethod
    def draw(self, screen):
        pass

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def setX(self, x):
        self.x = x

    def setY(self, y):
        self.y = y