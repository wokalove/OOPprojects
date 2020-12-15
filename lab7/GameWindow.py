import pygame ,sys

from pygame.locals import *

class Construction(pygame.sprite.Sprite):
    def __init__(self,url):
        pygame.sprite.Sprite.__init__(self)

        load_img = pygame.image.load(url).convert()
        self.image = pygame.transform.scale(load_img, (200, 100))
        self.start_rect = self.image.get_rect()
        self.rect = self.start_rect
        

    def draw(self,window,position):
        self.x, self.y = position
        event = pygame.event.poll()
        self.rect = pygame.draw.rect(window,(255,0,0),(self.x,self.y,0,0))
        return self.image, self.rect


class Button:
    def __init__(self, image_dir, position):
        load_img = pygame.image.load(image_dir).convert()
        self.image = pygame.transform.scale(load_img, (100, 50))
        self.rect = self.image.get_rect(topleft=position)
        
    
    def button_on_click(button, event):
        if event.type == 1:
            if self.rect.collidepoint(event.pos):
                self.button_action()

    def button_action(self):
        print("You push Goodbye button")
 
 
def display_label(window,label, position,size):
    main_font = pygame.font.SysFont("comicsans",size)
    user_money = main_font.render(label,1,(255,255,255))
    window.blit(user_money,position)



pygame.init() 
   
white = (255, 255, 255) 
X = 800
Y = 600
money = 2000

display_surface = pygame.display.set_mode((X, Y )) 

pygame.display.set_caption('Game') 

button1= Button(r'C:\GitRepo\Object_Oriented_Techniques\lab7\img\Mint.png',(70,70))


bg = pygame.image.load(r'C:\GitRepo\Object_Oriented_Techniques\lab7\img\mapa.jpg') 
background = pygame.transform.scale(bg, (800, 600))

image = pygame.image.load(r'C:\GitRepo\Object_Oriented_Techniques\lab7\img\Mint.png').convert()
start_rect = image.get_rect()
image_rect = start_rect

building = Construction(r'C:\GitRepo\Object_Oriented_Techniques\lab7\img\Mint.png')


while True : 
    event = pygame.event.poll()
    keyinput = pygame.key.get_pressed()

    display_surface.fill(white) 
    display_surface.blit(background, (0, 0)) 

    display_label(background,f"Money savings: {money}",(10,10),50)

    button1.button_on_click(event)
    display_surface.blit(button1.image, button1.rect)
    display_label(background,"Mint",(80,150),30)
    

    for event in pygame.event.get() : 
        
        if keyinput[pygame.K_ESCAPE]:
            raise SystemExit
        elif event.type == pygame.QUIT:
            pygame.quit() 
            quit()
        elif event.type == pygame.MOUSEBUTTONUP:
            position = pygame.mouse.get_pos()
            print(position)
            image, image_rect = building.draw(display_surface,position)
            
        display_surface.blit(image,image_rect)

        pygame.display.flip()  
             