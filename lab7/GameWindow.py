import pygame ,sys
from pygame.locals import *
from Buildings import *
import time
import threading 
import pygame_menu
import pickle
import concurrent.futures
from multiprocessing.pool import ThreadPool

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
         


def display_label(window,label, position,size):
    result = type(position) is tuple
    main_font = pygame.font.SysFont("lato",size)
    name = main_font.render(label,1,(255,255,255))
    if result:
        x, y = position
        window.blit(name,(x,y))
    else:
        window.blit(name,position)

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

    while pause:
        display_buildings(gameDisplay,buildings)
        display_label(gameDisplay,f"Money savings: {user1.money}",(10,0),50)

        for event in pygame.event.get():
            
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        if (time.time() - start_time) > 1.0:
            print(time.time() - start_time)
            pause = 0
        pygame.display.update()  

def save_game(user,created_objects):
    with open('data/savefile.dat', 'wb') as f:
        pickle.dump(user, f, protocol=2)


def read_game():    
    # loading
    with open('data/savefile.dat', 'rb') as f:
        user = pickle.load(f)
    return user
def receive_val():
    x = self.generate_income_periodically
    threading.Timer(10, x).start()
    return x

def start_game(user_name,surface):
    pygame.init() 
    
    X = 800
    Y = 600
    
    #display_surface = pygame.display.set_mode((X, Y )) 
    display_surface = surface
    pygame.display.set_caption('Game') 
    color = (0,0,0)

    #map
    img_bg_path = FOLDER_PATH + r'\mapa.jpg'
    bg = pygame.image.load(img_bg_path) 
    background = pygame.transform.scale(bg, (X, Y))

    img_mint_path = FOLDER_PATH + r'\mint.png'
    #menu buttons
    x_s = 200
    x_q =500
    y_btn_menu = 530

        
    '''save_btn = Button('Save',img_mint_path,(x_s,y_btn_menu))
    quit_btn = Button('Quit',img_mint_path,(x_q,y_btn_menu)) 
    '''


    #Building Buttons
    img_mint_path = FOLDER_PATH + r'\mint.png'
    button1= Button('Mint',img_mint_path,(70,70))


    img_hut_path = FOLDER_PATH + r'\hut.jpg'
    button2= Button('Hut',img_hut_path,(200,70))

    img_gold_path = FOLDER_PATH + r'\gold_mine.jpg'
    button3= Button('Gold Mine',img_gold_path,(330,70))

    img_quarry_path = FOLDER_PATH + r'\quarry.jpg'
    button4= Button('Quarry',img_quarry_path,(460,70))

    img_sawmill_path = FOLDER_PATH + r'\sawmill.jfif'
    button5= Button('Sawmill',img_sawmill_path,(590,70))

  

    area = pygame.Rect(0, 170, 800, 450)

    #TODO POPRAWNE user1 = User(user_name.get_value())
    user1 = User(user_name)
    print("Downloaded name:",user1.nickname)
    buildings =[]

    building_buttons = [button1, button2, button3, button4,button5]

    display_label(background,"Mint",(90,130),20)
    display_label(background,"Hut",(225,130),20)
    display_label(background,"Gold Mine",(330,130),20)
    display_label(background,"Quarry",(480,130),20)
    display_label(background,"Sawmill",(600,130),20)
    
    x_income = 0
    y_income = 0
    return_val = ''
    no_money =''
    income = 0

    return_income = {
        'return_mint':'',
        'return_hut':'',
        'return_gold':'',
        'return_quarry':'',
        'return_sawmill':'',

    }

    income_position ={
        'mint':(0,0),
        'hut':(0,0),
        'gold':(0,0),
        'quarry':(0,0),
        'sawmill':(0,0)

    }
    return_val =''
    return_sawmill =''

    x_sawmill = 0
    y_sawmill = 0
    
    while True :
        keyinput = pygame.key.get_pressed()

        
        display_surface.blit(background, (0, 0)) 
        
        pygame.draw.rect(display_surface, color, pygame.Rect(0, 0, 800, 100)) 
        
        save_btn = pygame.draw.rect(display_surface, color,(200,530,100,50))
        quit_btn = pygame.draw.rect(display_surface, color,(500,530,100,50))



        #display buttons
        for button in building_buttons:
            display_surface.blit(button.image,button.rect)

       
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
                print(type(position))
                
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
                        price = user1.buy_building(clicked_building[0])
                        
                        if price:
                            building = Mint('Mint',price)
                            user1.money-=price
                            mint_income = Income(building)
                            call_template_method(mint_income)

                            x_income, y_income= position
                            pool = ThreadPool(processes=5)
                            async_result = pool.apply_async(hut_income.generate_income_periodically) # tuple of args for foo
                            return_val = async_result.get()
                            return_val = str(return_val)
                            
                        else:
                            building = None 
                            no_money = "Not enough money!"
                            display_label(display_surface,no_money,(470,15),30)
                            paused(display_surface, buildings, user1)        
                            print(no_money)

                
                    elif clicked_building[0] == "Gold Mine":
                        price = user1.buy_building(clicked_building[0])
                        if price:
                            building = GoldMine('Gold Mine',price)
                            user1.money-= price
                            goldmine_income = Income(building)
                            #call_template_method(goldmine_income)
        
                            pool = ThreadPool(processes=5)
                            async_result = pool.apply_async(hut_income.generate_income_periodically) # tuple of args for foo
                            return_val = async_result.get()
                            return_val = str(return_val)
                            return_income['gold_income'] = return_val
                        else:
                            building = None
                            no_money = "Not enough money"
                            display_label(display_surface,no_money,(470,15),30)
                            paused(display_surface, buildings, user1) 
                            print(no_money)

                    elif clicked_building[0] == "Hut":
                        price = user1.buy_building(clicked_building[0])
                        if price:
                            building = Hut('Hut',price)
                            user1.money-= price
                            hut_income = Income(building)
                            #call_template_method(hut_income)
                            x_income, y_income= position
                            pool = ThreadPool(processes=5)
                            async_result = pool.apply_async(hut_income.generate_income_periodically) # tuple of args for foo
                            return_val = async_result.get()
                            return_val = str(return_val)
                            return_income['hut_income'] = return_val
                        else:
                            building = None
                            no_money = "Not enough money"
                            display_label(display_surface,no_money,(470,15),30)
                            paused(display_surface, buildings, user1) 
                            print(no_money)

                    elif clicked_building[0] == "Quarry":
                        price = user1.buy_building(clicked_building[0])
                        if price:
                            building = Quarry('Quarry',price)
                            user1.money-= price
                            hut_income = Income(building)
                            #call_template_method(hut_income)

                            x_income, y_income= position
                            pool = ThreadPool(processes=5)
                            async_result = pool.apply_async(hut_income.generate_income_periodically) # tuple of args for foo
                            return_val = async_result.get()
                            return_val = str(return_val)
                        else:
                            building = None
                            no_money = "Not enough money"
                            display_label(display_surface,no_money,(470,15),30)
                            paused(display_surface, buildings, user1) 
                            print(no_money)

                    elif clicked_building[0] == "Sawmill":
                        price = user1.buy_building(clicked_building[0])
                        if price:
                            building = Sawmill('Sawmill',price)
                            user1.money-= price
                            hut_income = Income(building)
                            #call_template_method(hut_income)
                            
                            x_sawmill, y_sawmill= position
                            income_position['sawmill'] = (x_sawmill+200,y_sawmill+100)
                            
                            pool = ThreadPool(processes=5)
                            async_result = pool.apply_async(hut_income.generate_income_periodically) # tuple of args for foo
                            return_sawmill = async_result.get()
                            return_sawmill = str(return_sawmill)
                            sawmill = income_position.get('sawmill')
                            print("CO DAJE SAWMILL",type(income_position.get('sawmill')))
                            print("income:",return_sawmill)
                            
                        else:
                            building = None
                            no_money = "Not enough money"
                            display_label(display_surface,no_money,(470,15),30)
                            paused(display_surface, buildings, user1) 
                            print(no_money)

                    #TODO kombo!
                    if building:
                        buildings.append([building.image,position])
            
            
            display_buildings(display_surface,buildings)
            save_game(user1,building_buttons)

            display_label(display_surface,return_val,(x_income+70,y_income+100),30)
            display_label(display_surface,return_sawmill,(x_sawmill+70,y_sawmill+100),30)
            display_label(display_surface, return_income.get("sawmill_income", ""),income_position.get('sawmill'),30)
            display_label(display_surface, return_income.get("gold_income", ""),(x_sawmill+70,y_sawmill+100),30)
            
            display_label(display_surface,f"Money savings: {user1.money}",(10,0),50)


            pygame.display.update()  

if __name__ == "__main__":
    start_game('Ola',pygame.display.set_mode((800, 600 )) )
    print(pygame.font.get_fonts())