import pygame

pygame.init()
screen = pygame.display.set_mode((800,600))
running = True

pygame.display.set_caption("Ancient")
#Game loop
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    screen.fill((89, 86, 76))
    pygame.display.update()