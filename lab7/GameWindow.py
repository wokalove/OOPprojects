import pygame ,sys
from pygame.locals import *
from Buildings import *


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
    def __init__(self,name, image_dir, position):
        self.name = name
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

def display_buildings(surface,arr):
    for a in arr:
        surface.blit(a[0],a[1])

def check_status(buttons):
    for b in buttons:
        if b.clicked == True:
            return [b.name,True]
    return ['',False]

pygame.init() 
   
white = (255, 255, 255) 
X = 800
Y = 600
money = 2000

display_surface = pygame.display.set_mode((X, Y )) 

pygame.display.set_caption('Game') 

img_mint_path = FOLDER_PATH + r'\mint.png'
button1= Button('Mint',img_mint_path,(70,70))


img_hut_path = FOLDER_PATH + r'\hut.png'
button2= Button('Hut',img_hut_path,(200,70))

img_bg_path = FOLDER_PATH + r'\mapa.jpg'
bg = pygame.image.load(img_bg_path) 
background = pygame.transform.scale(bg, (800, 600))

area = pygame.Rect(0, 170, 800, 450)

user1 = User('Ola')
buildings =[]

building_buttons = [button1, button2]

no_money =''

while True :
    keyinput = pygame.key.get_pressed()

    display_surface.fill(white) 
    display_surface.blit(background, (0, 0)) 

    display_surface.blit(button1.image, button1.rect)
    display_label(background,"Mint",(80,120),30)

    display_surface.blit(button2.image, button2.rect)
    display_label(background,"Hut",(225,120),30)
    pygame.draw.rect(display_surface, (100, 200, 70), area)
    
    display_label(background,no_money,(50,400),3)

    for event in pygame.event.get() :     
        
        if keyinput[pygame.K_ESCAPE]:
            raise SystemExit
        elif event.type == pygame.QUIT:
            pygame.quit() 
            quit()

        elif event.type == pygame.MOUSEBUTTONDOWN: #albo up, nie czuje różnicy
            position = pygame.mouse.get_pos()
            print(position)
            
            for button in building_buttons:
                if button.rect.collidepoint(position):
                    print('clicked on:',button.name)
                    for button_i in building_buttons:
                        if button == button_i:
                            continue
                        if button_i.clicked == True:
                            button_i.clicked = False

                    clicked = button.button_status()
            
            clicked_building = check_status(building_buttons)
            if clicked_building[1] and area.collidepoint(position):

                if clicked_building[0] == "Mint":
                    price = 3000
                    
                    building = Mint('Mint',price,img_mint_path)
                    if user1.buy_building(building):
                        user1.money-=price
                        mint_income = Income(building)
                        call_template_method(mint_income)
                    else:
                        no_money = "Not enough money"
                        print(no_money)

            
                elif clicked_building[0] == "Hut":
                    price =200

                    building = Hut('Hut',price,img_hut_path)
                    if user1.buy_building(building):
                        user1.money-=price
                        mint_income = Income(building)
                        call_template_method(mint_income)
                    
                buildings.append([building.image,position])
                      
        
        display_buildings(display_surface,buildings)
        display_label(display_surface,f"Money savings: {user1.money}",(10,10),50)
            
            
   

        pygame.display.flip()  
             