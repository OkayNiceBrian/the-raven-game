import pygame
import sys
from Characters.BoneDruid.BoneDruid import BoneDruid
import util.GameStates as states
from Entity import Entity

class Game:

    def __init__(self, screen, clock):
        self.screen = screen
        self.clock = clock
        self.entities = []

        self.state = states.player1Menu

        self.player1 = BoneDruid()
        self.player2 = BoneDruid()

    def update(self):
        for e in self.entities:
            e.update()

    def draw(self):
        for e in self.entities:
            e.draw(self.screen)

    def leftMousePressed(self):
        True