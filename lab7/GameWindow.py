import pygame
import pygame_menu

pygame.init()
surface = pygame.display.set_mode((800, 600))


def new_the_game():
    # Do the job here !
    menu.add_text_input('Name :', default='')
    
    
def read_the_game():
    # Do the job here !
    pass
menu = pygame_menu.Menu(600, 800, 'Welcome',
                       theme=pygame_menu.themes.THEME_BLUE)


menu.add_button('New game', new_the_game)
menu.add_button('Read game', read_the_game)
menu.add_button('Quit', pygame_menu.events.EXIT)




menu.mainloop(surface)