import pygame ,sys
from pygame.locals import *
from Buildings import *
import time
import threading 
FOLDER_PATH = r'C:\GitRepo\Object_Oriented_Techniques\lab7\img'

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

def paused(gameDisplay,buildings, user1):

    pause = 1
    start_time = time.time()
    #largeText = pygame.font.SysFont("comicsansms",115)
    #TextSurf, TextRect = text_objects("Paused", largeText)
    #TextRect.center = ((display_width/2),(display_height/2))
    #gameDisplay.blit(TextSurf, TextRect)
    

    while pause:


        display_buildings(gameDisplay,buildings)
        display_label(gameDisplay,f"Money savings: {user1.money}",(10,10),50)

        for event in pygame.event.get():
            
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        if (time.time() - start_time) > 1.0:
            print(time.time() - start_time)
            pause = 0
        pygame.display.update()  
        


pygame.init() 
   
white = (255, 255, 255) 
X = 800
Y = 600
money = 2000

display_surface = pygame.display.set_mode((X, Y )) 
pygame.display.set_caption('Game') 

#Building Buttons
img_mint_path = FOLDER_PATH + r'\mint.png'
button1= Button('Mint',img_mint_path,(70,70))


img_hut_path = FOLDER_PATH + r'\hut.png'
button2= Button('Hut',img_hut_path,(200,70))

img_gold_path = FOLDER_PATH + r'\gold_mine.jpg'
button3= Button('Gold Mine',img_gold_path,(330,70))

img_quarry_path = FOLDER_PATH + r'\quarry.png'
button4= Button('Quarry',img_quarry_path,(460,70))

img_sawmill_path = FOLDER_PATH + r'\sawmill.jfif'
button5= Button('Sawmill',img_sawmill_path,(590,70))

#map
img_bg_path = FOLDER_PATH + r'\mapa.jpg'
bg = pygame.image.load(img_bg_path) 
background = pygame.transform.scale(bg, (X, Y))

area = pygame.Rect(0, 170, 800, 450)

user1 = User('Ola')
buildings =[]

building_buttons = [button1, button2, button3, button4]

no_money =''

while True :
    keyinput = pygame.key.get_pressed()

    display_surface.fill(white) 
    display_surface.blit(background, (0, 0)) 

    #display button
    display_surface.blit(button1.image, button1.rect)
    display_label(background,"Mint",(90,130),30)

    display_surface.blit(button2.image, button2.rect)
    display_label(background,"Hut",(225,130),30)

    display_surface.blit(button3.image, button3.rect)
    display_label(background,"Gold Mine",(330,130),30)

    display_surface.blit(button4.image, button4.rect)
    display_label(background,"Quarry",(480,130),30)

    display_surface.blit(button5.image, button5.rect)
    display_label(background,"Sawmill",(600,130),30)

    #display map
    pygame.draw.rect(display_surface, (100, 200, 70), area,-1,-1)

    for event in pygame.event.get() :     
        
        if keyinput[pygame.K_ESCAPE]:
            raise SystemExit
        elif event.type == pygame.QUIT:
            pygame.quit() 
            quit()

        elif event.type == pygame.MOUSEBUTTONDOWN:
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
                    
                    if user1.buy_building(clicked_building[0]):
                        building = Mint('Mint',price,img_mint_path)
                        user1.money-=price
                        mint_income = Income(building)
                        call_template_method(mint_income)
                        display_label(display_surface,no_money,(380,15),30)
                    else:
                        building = None 
                        no_money = "Not enough money!"
                        display_label(display_surface,no_money,(380,15),30)
                        paused(display_surface, buildings, user1)        
                        #pygame.time.delay(2000)
                        print(no_money)

            
                elif clicked_building[0] == "Hut":
                    price = 200
                    if user1.buy_building(clicked_building[0]):
                        building = Hut('Hut',price,img_hut_path)
                        user1.money-= price
                        mint_income = Income(building)
                        call_template_method(mint_income)
                    else:
                        building = None
                        no_money = "Not enough money"
                        display_label(display_surface,no_money,(380,15),30)
                        paused(display_surface, buildings, user1) 
                        print(no_money)

                #TODO reszta budowli i kombo!
                if building:
                    buildings.append([building.image,position])
        
        
        display_buildings(display_surface,buildings)
        display_label(display_surface,f"Money savings: {user1.money}",(10,10),50)
            
            
   

        pygame.display.update()  
             