import pygame
import sys
from Entity import Entity

class Game:

    def __init__(self, screen, clock):
        self.screen = screen
        self.clock = clock
        self.entities = [Entity]

    def update(self):
        for e in self.entities:
            e.update()

    def draw(self):
        for e in self.entities:
            e.draw(self.screen)

    def leftMousePressed(self):
        True