import pygame ,sys
from pygame.locals import *


FOLDER_PATH = r'C:\GitRepo\Object_Oriented_Techniques\lab7\img'


class Construction(pygame.sprite.Sprite):
    def __init__(self,url):
        pygame.sprite.Sprite.__init__(self)

        load_img = pygame.image.load(url).convert()
        self.image = pygame.transform.scale(load_img, (200, 100))
        self.start_rect = self.image.get_rect()
        self.rectangle = self.start_rect

    def draw(self,window,position):
        pass
     


class Button:
    def __init__(self, image_dir, position):
        load_img = pygame.image.load(image_dir).convert()
        self.image = pygame.transform.scale(load_img, (100, 50))
        self.rect = self.image.get_rect(topleft=position)
        self.clicked = False
        
    def button_status(self):
        self.clicked = not self.clicked
        return self.clicked
         
    def display(self):
        display_surface.blit(self.image,self.rect)
 

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

img_mint_path = FOLDER_PATH + r'\mint.png'
button1= Button(img_mint_path,(70,70))


img_hut_path = FOLDER_PATH + r'\hut.png'
button2= Button(img_hut_path,(200,70))

img_bg_path = FOLDER_PATH + r'\mapa.jpg'
bg = pygame.image.load(img_bg_path) 
background = pygame.transform.scale(bg, (800, 600))

area = pygame.Rect(0, 170, 800, 450)


while True : 
    keyinput = pygame.key.get_pressed()

    display_surface.fill(white) 
    display_surface.blit(background, (0, 0)) 

    display_label(background,f"Money savings: {money}",(10,10),50)

    display_surface.blit(button1.image, button1.rect)
    display_label(background,"Mint",(80,120),30)


    display_surface.blit(button2.image, button2.rect)
    display_label(background,"Hut",(225,120),30)
    
    x,y = 0,0

    for event in pygame.event.get() : 
        pygame.draw.rect(display_surface, (100, 200, 70), area)
        
        
        if keyinput[pygame.K_ESCAPE]:
            raise SystemExit
        elif event.type == pygame.QUIT:
            pygame.quit() 
            quit()

        elif event.type == pygame.MOUSEBUTTONDOWN: #albo up, nie czuje różnicy
            x,y = event.pos

            if button1.rect.collidepoint(x,y):
                print('clicked on mint')
                
                clicked = button1.button_status()
                print(clicked)
                if clicked:
                    print("Mint True")
                    building = Construction(img_mint_path)
                    
                    display_surface.blit(building.image,building.rectangle)
                    x, y = position
                    pygame.draw.rect(display_surface,(255,0,0),(150,450,0,0))         
                    
        
            elif button2.rect.collidepoint(x,y):
                print('Clicked on hut')
                clicked = button2.button_status()
                
                if clicked:
                    print("True in hut")
                    position = pygame.mouse.get_pos()
                    if event.button == 1:  # Left mouse button.                      

                        print("True in hut ==1")
                        (x, y)= position
                        if area.collidepoint(position):
                            print('Area clicked.')
    
                            building = Construction(img_hut_path)
                            
                            display_surface.blit(building.image,building.rectangle)
                            x, y = position
                            pygame.draw.rect(display_surface,(255,0,0),(150,450,0,0))         
                            
            
            print(position)
   

        pygame.display.flip()  
             