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
        True

    def draw(self):
        if (self.state == states.player1Menu):
            self.drawPlayerMenu(self.player1)

    def leftMousePressed(self):
        True

    def drawPlayerMenu(self, character):
        textColor = (255, 255, 255)
        titleWeight = 32
        subWeight = 24

        self.drawText(character.name, 50, 40, textColor, titleWeight)
        
        self.drawText("Abilities:", 100, 100, textColor, titleWeight)
        
        for i in range(len(character.abilities)):
            ability = character.abilities[i]
            self.drawText(ability.name + " (" + str(ability.level) + ")", 150, 150 + (40 * i), textColor, subWeight)

        self.drawText("Stats:", 500, 100, textColor, titleWeight)

        self.drawText("Health: " + str(character.health), 550, 150, textColor, subWeight)
        self.drawText("Physical: " + str(character.physical), 550, 190, textColor, subWeight)
        self.drawText("Magic: " + str(character.magic), 550, 230, textColor, subWeight)
        self.drawText("Phys. Resist: " + str(character.phys_resist), 550, 270, textColor, subWeight)
        self.drawText("Mag. Resist: " + str(character.mag_resist), 550, 310, textColor, subWeight)

        self.drawText(character.description, 100, 400, textColor, subWeight)
        
    def drawText(self, str, x, y, color, fontWeight):
        font = pygame.font.Font('freesansbold.ttf', fontWeight)
        characterLimit = 80
        if (len(str) > characterLimit):
            words = str.split(" ")
            wordIndex = 0
            line = 0
            while (wordIndex < len(words)):
                lineString = ""
                while (len(lineString) < characterLimit):
                    if (wordIndex >= len(words) or len(lineString + words[wordIndex]) > characterLimit):
                        break
                    lineString = lineString + words[wordIndex] + " "
                    wordIndex = wordIndex + 1
                text = font.render(lineString, True, color)
                textRect = text.get_rect()
                textRect.bottomleft = (x, y + (30 * line))
                self.screen.blit(text, textRect)
                line = line + 1
        else: 
            text = font.render(str, True, color)
            textRect = text.get_rect()
            textRect.bottomleft = (x, y)
            self.screen.blit(text, textRect)

    