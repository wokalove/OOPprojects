import pygame ,sys

from pygame.locals import *

class Construction(pygame.sprite.Sprite):
    def __init__(self,position):
        pygame.sprite.Sprite.__init__(self)
        load_img = pygame.image.load(r'C:\GitRepo\Object_Oriented_Techniques\lab7\img\Mint.png').convert()
        self.image = pygame.transform.scale(load_img, (200, 100))
        self.start_rect = self.image.get_rect()
        self.rect = self.start_rect
        self.x,self.y = position

    def draw(self,window):
        #pygame.draw.rect(window,(255,0,0),(self.x,self.y,0,0))
        event = pygame.event.poll()
        self.rect.center = (self.x,self.y)
        self.rec = self.start_rect.move(event.pos)
        window.blit(self.image,self.rect)

        pygame.display.flip()

def display_label(window):
    main_font = pygame.font.SysFont("comicsans",50)
    user_money = main_font.render(f"Money savings:{money}",1,(255,255,255))
    window.blit(user_money,(10,10))
    pygame.display.update()


pygame.init() 
   
white = (255, 255, 255) 
X = 800
Y = 600
money = 2000

display_surface = pygame.display.set_mode((X, Y )) 

pygame.display.set_caption('Game') 


bg = pygame.image.load(r'C:\GitRepo\Object_Oriented_Techniques\lab7\img\mapa.jpg') 
background = pygame.transform.scale(bg, (800, 600))

image = pygame.image.load(r'C:\GitRepo\Object_Oriented_Techniques\lab7\img\Mint.png').convert()
start_rect = image.get_rect()
image_rect = start_rect

while True : 
    event = pygame.event.poll()
    keyinput = pygame.key.get_pressed()
    display_surface.blit(image, (0, 0)) 
    display_surface.fill(white) 
    display_surface.blit(background, (0, 0)) 
    display_label(background)
  
    for event in pygame.event.get() : 
        
        if keyinput[pygame.K_ESCAPE]:
            raise SystemExit
        elif event.type == pygame.QUIT:
            pygame.quit() 
            quit()
        elif event.type == pygame.MOUSEBUTTONUP:
            position = pygame.mouse.get_pos()
            print(position)
            image_rect = start_rect.move(event.pos)
            
        display_surface.blit(image, image_rect)
            #building = Construction(position)
            #building.draw(display_surface)

        pygame.display.flip()  
             