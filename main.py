import pygame, sys
import time
from pygame.locals import *
import cgitb
 
# Initialize program
pygame.init()
 
# Assign FPS a value
FPS = 30
FramePerSec = pygame.time.Clock()
 
# Setting up color objects
BLUE  = (0, 140, 240)
RED   = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

global moving 
moving = True
 
# Setup a 300x300 pixel display with caption
DISPLAYSURF = pygame.display.set_mode((950,180))
pygame.display.set_caption("Example")
 
# Creating Lines and Shapes
"""pygame.draw.line(DISPLAYSURF, BLUE, (150,130), (130,170))
pygame.draw.line(DISPLAYSURF, BLUE, (150,130), (170,170))
pygame.draw.line(DISPLAYSURF, GREEN, (130,170), (170,170))
pygame.draw.circle(DISPLAYSURF, BLACK, (100,50), 30)
pygame.draw.circle(DISPLAYSURF, BLACK, (200,50), 30)
pygame.draw.rect(DISPLAYSURF, RED, (100, 200, 100, 50), 2)
pygame.draw.rect(DISPLAYSURF, BLACK, (110, 260, 80, 5))"""


SnowImgStill = pygame.image.load('snowstill.png')
SnowImgWalk = pygame.image.load('snowwalk.png')
ParadiseBackground = pygame.image.load('paradise.png')

SnowImgWalk = pygame.transform.scale(SnowImgWalk, (160,160))
SnowImgStill = pygame.transform.scale(SnowImgStill, (160,160))
ParadiseBackground = pygame.transform.scale(ParadiseBackground, (950, 180))

def walk(x,y):
    DISPLAYSURF.blit(SnowImgWalk, (x,y))
    pygame.display.update()

def still(x,y):
    DISPLAYSURF.blit(SnowImgStill, (x,y))
    pygame.display.update()


def move(x,y):
    global moving
    if moving:
        still(x,y)
        moving = False
    else:
        walk(x,y)
        moving = True
    
x = 0
y = 0
snowx = 10
snowy = 60
step = 8

while True:
    #time.sleep(0.5)
    DISPLAYSURF.blit(ParadiseBackground, (x,y))
    
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    key_input = pygame.key.get_pressed()   
    if key_input[pygame.K_LEFT]:
        if x < 0:
            x += step
        elif snowx > 0:
            snowx -= step
        move(snowx,snowy)
    if key_input[pygame.K_RIGHT]:
        if x > -344:
            x -= step
        elif snowx < 420:
            snowx += step
        move(snowx,snowy)

    still(snowx,snowy)

    print(x,y)
    
    time.sleep(0.1)

    #walk(150,150)
    pygame.display.update()
   
    FramePerSec.tick(FPS)