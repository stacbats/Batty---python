# ***************************************************************
# resources via internet & Sloane Kelly
# looking to build a Brick & Ball Game
# ***************************************************************

import pygame, os,sys       # making sure resources are inmported
from pygame.locals import *

# Variable

height = 800
width = 600
# end of Variables

pygame.init()
fpsClock = pygame.time.Clock()
mainSurface = pygame.display.set_mode((height, width))
pygame.display.set_caption('batty')

teal = pygame.Color(0,128,128)      # teal colour

# bat init

bat = pygame.image.load('bat.png')
playerY = 540               # x axis only - higher the number the further down we are
batRect = bat.get_rect()
mousex, mousey = (0, playerY)

# ball init

ball = pygame.image.load('ball.png')        # load the image
ballRect = ball.get_rect()                  # capture rectangle
ballStartY = 200                            # set up co ordinate starting pos
ballSpeed = 3                               # the balls speed
ballServed = False                          # has the ball been served or not yet
bx, by = (24, ballStartY)
sx, sy = (ballSpeed, ballSpeed)
ballRect.topleft = (bx, by)

# brick init

while True:
    mainSurface.fill(teal)
    # brick draw

    # bat & ball draw
    mainSurface.blit(bat, batRect)
    mainSurface.blit(ball, ballRect)

    # events

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == MOUSEMOTION:
            mousex, mousey = event.pos
            if (mousex < 800 - 55):
                batRect.topleft = (mousex, playerY)
        else:
                batRect.topleft = (800 - 55, playerY)

    # main game logic

    # collision detection

    pygame.display.update()
    fpsClock.tick(30)