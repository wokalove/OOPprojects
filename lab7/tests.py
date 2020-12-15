import pygame
import sys
import os
from pygame.locals import *

pygame.init() # initialize pygame
clock = pygame.time.Clock()
screen = pygame.display.set_mode((600,500))

# os.path.join properly forms a cross-platform relative path
# by joining directory names

bg =  pygame.image.load(r'C:\GitRepo\Object_Oriented_Techniques\lab7\img\mapa.jpg').convert()


pygame.mouse.set_visible(0)

ship = pygame.image.load(r'C:\GitRepo\Object_Oriented_Techniques\lab7\img\Mint.png').convert()
ship_top = screen.get_height() - ship.get_height()
ship_left = screen.get_width()/2 - ship.get_width()/2
screen.blit(ship, (ship_left,ship_top))

shot = pygame.image.load(r'C:\GitRepo\Object_Oriented_Techniques\lab7\img\Mint.png') 
shoot_y = 0


pygame.display.set_caption('galaxy invaders')

# fix indentation

while True:
    clock.tick(60)
    screen.blit(bg, (0,0))
    x,y = pygame.mouse.get_pos()
    screen.blit(ship, (x-ship.get_width()/2, ship_top))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == MOUSEBUTTONDOWN:
            shoot_y = 500
            shoot_x = x

    if shoot_y > 0:
        screen.blit(shot, (shoot_x, shoot_y))
        shoot_y -= 10

    pygame.display.update()