from cmath import pi, sqrt, sin, cos
from math import atan2
import sys
import pygame
from Game import Game
pygame.init()

size = width, height = 1280, 720
black = 0, 0, 0

screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()

leftPressed = False
rightPressed = False
upPressed = False
downPressed = False
spacePressed = False
leftMousePressed = False
middleMousePressed = False
rightMousePressed = False

entities = []

game = Game(screen, clock)

# earthImage = "../assets/earth.png"
# ballImage = "../assets/ball.png"

# entities.append(earth)
# entities.append(meteor)

gameplayPaused = True

        #pygame.draw.circle(screen, (200, 200, 50, 50), ((fliers[0].getX() + viewXOffset) + xdist + (xdist * i), (fliers[0].getY() + viewYOffset) + ydist + (ydist * i)), 1)

while 1:
    # Events
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                leftPressed = True
            if event.key == pygame.K_RIGHT:
                rightPressed = True
            if event.key == pygame.K_UP:
                upPressed = True
            if event.key == pygame.K_DOWN:
                downPressed = True
            if event.key == pygame.K_SPACE:
                spacePressed = True
                gameplayPaused = not gameplayPaused
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                leftPressed = False
            if event.key == pygame.K_RIGHT:
                rightPressed = False
            if event.key == pygame.K_UP:
                upPressed = False
            if event.key == pygame.K_DOWN:
                downPressed = False
            if event.key == pygame.K_SPACE:
                spacePressed = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mousePressed = pygame.mouse.get_pressed()
            if mousePressed[0]:
                leftMousePressed = True
                print("left mouse pressed")
            if mousePressed[1]:
                middleMousePressed = True
                print("middle mouse pressed")
            if mousePressed[2]:
                rightMousePressed = True
                print("right mouse pressed")
        if event.type == pygame.MOUSEBUTTONUP:
            if pygame.mouse.get_pressed()[0]:
                leftMousePressed = False
                print("left mouse released")
            if pygame.mouse.get_pressed()[1]:
                middleMousePressed = False
                print("middle mouse released")
            if pygame.mouse.get_pressed()[2]:
                rightMousePressed = False
                print("right mouse released")

    # Update
    speedConstant = clock.tick(60)

    if spacePressed:
        True

    if gameplayPaused:
        True

    if leftMousePressed:
        True

    if not gameplayPaused:
        for e in entities:
            e.update()

    game.update()
            
    leftMousePressed = False
    middleMousePressed = False
    rightMousePressed = False    

    # Draw
    screen.fill(black)
    
    for e in entities:
        e.rect.x = e.x 
        e.rect.y = e.y
        screen.blit(e.image, e.rect)

    game.draw()
    
    pygame.display.flip()
    

