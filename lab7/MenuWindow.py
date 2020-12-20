# Import libraries
import sys

sys.path.insert(0, '../../')

import os
import pygame
import pygame_menu

from random import randrange

from GameWindow  import *
# -----------------------------------------------------------------------------
# Constants and global variables
# -----------------------------------------------------------------------------
ABOUT = ['Game: Śląski świat ',
         'Author: Ola Duda',
         '',  # new line
         'Email: oladuda1999@gmail.com']
DIFFICULTY = ['EASY']
FPS = 60.0
WINDOW_SIZE = (800, 600)

clock = None  # type: pygame.time.Clock
main_menu = None  # type: pygame_menu.Menu
surface = None  # type: pygame.Surface


# -----------------------------------------------------------------------------
# Methods
# -----------------------------------------------------------------------------
  

def play_function( font, test=False):
    # Define globals
    global main_menu
    global clock
    global play_menu
    
    #start_game()

    game_menu = pygame_menu.Menu(
        height=WINDOW_SIZE[1],
        onclose=pygame_menu.events.DISABLE_CLOSE,
        title='Game Menu',
        width=WINDOW_SIZE[0] ,
    )
    
    
    # Reset main menu and disable
    # You also can set another menu, like a 'pause menu', or just use the same
    # main_menu as the menu that will check all your input.
    main_menu.disable()
    main_menu.reset(1)

    user_name = game_menu.add_text_input('First name: ', default='')
    game_menu.add_button('Play',start_game,user_name,surface)
    game_menu.add_button('Back',pygame_menu.events.BACK)
    game_menu.mainloop(surface)

    while True:
        
        # noinspection PyUnresolvedReferences
        clock.tick(60)

        # Application events
        events = pygame.event.get()
        for e in events:
            if e.type == pygame.QUIT:
                exit()
            elif e.type == pygame.KEYDOWN:
                if e.key == pygame.K_ESCAPE:
                    main_menu.enable()

                    # Quit this function, then skip to loop of main-menu on line 317
                    return

        
        pygame.display.flip()

        # If test returns
        if test:
            break


def read_game():    
    # loading
    with open('data/savefile.dat', 'rb') as f:
        user = pickle.load(f)
    return user
    
def main_background():
    """
    Function used by menus, draw on background while menu is active.
    :return: None
    """
    global surface
    surface.fill((128, 0, 128))


def main(test=False):
    """
    Main program.
    :param test: Indicate function is being tested
    :type test: bool
    :return: None
    """

    # -------------------------------------------------------------------------
    # Globals
    # -------------------------------------------------------------------------
    global clock
    global main_menu
    global surface

    # -------------------------------------------------------------------------
    # Init pygame
    # -------------------------------------------------------------------------
    pygame.init()
    os.environ['SDL_VIDEO_CENTERED'] = '1'

    # Create pygame screen and objects
    surface = pygame.display.set_mode(WINDOW_SIZE)
    pygame.display.set_caption('Example - Game Selector')
    clock = pygame.time.Clock()



    # -------------------------------------------------------------------------
    # Create menus: Play Menu
    # -------------------------------------------------------------------------
    play_menu = pygame_menu.Menu(
        height=WINDOW_SIZE[1] ,
        onclose=pygame_menu.events.DISABLE_CLOSE,
        title='Play Menu',
        width=WINDOW_SIZE[0] ,
    )

    submenu_theme = pygame_menu.themes.THEME_DARK.copy()
    submenu_theme.widget_font_size = 15
    play_submenu = pygame_menu.Menu(
        height=WINDOW_SIZE[1] ,
        theme=submenu_theme,
        title='Submenu',
        width=WINDOW_SIZE[0] ,
    )
    for i in range(30):
        play_submenu.add_button('Back {0}'.format(i), pygame_menu.events.BACK)
    play_submenu.add_button('Return to main menu', pygame_menu.events.RESET)

    play_menu.add_button('New game', play_function,pygame.font.Font(pygame_menu.font.FONT_FRANCHISE, 30))
   
    play_menu.add_button('Read game', play_submenu)
    play_menu.add_button('Return to main menu', pygame_menu.events.BACK)

    # -------------------------------------------------------------------------
    # Create menus:About
    # -------------------------------------------------------------------------
    about_theme = pygame_menu.themes.THEME_DARK.copy()
    about_theme.widget_margin = (0, 0)
    about_theme.widget_offset = (0, 0.05)

    about_menu = pygame_menu.Menu(
        height=WINDOW_SIZE[1] ,
        onclose=pygame_menu.events.DISABLE_CLOSE,
        theme=about_theme,
        title='About',
        width=WINDOW_SIZE[0] ,
    )
    for m in ABOUT:
        about_menu.add_label(m, align=pygame_menu.locals.ALIGN_LEFT, font_size=20)
    about_menu.add_label('')
    about_menu.add_button('Return to menu', pygame_menu.events.BACK)

    # -------------------------------------------------------------------------
    # Create menus: Main
    # -------------------------------------------------------------------------
    main_theme = pygame_menu.themes.THEME_DARK.copy()
    main_theme.menubar_close_button = False  # Disable close button

    main_menu = pygame_menu.Menu(
        height=WINDOW_SIZE[1],
        onclose=pygame_menu.events.DISABLE_CLOSE,
        theme=main_theme,
        title='Main Menu',
        width=WINDOW_SIZE[0] 
    )

    main_menu.add_button('Play', play_menu)
    main_menu.add_button('About', about_menu)
    main_menu.add_button('Quit', pygame_menu.events.EXIT)

    # -------------------------------------------------------------------------
    # Main loop
    # -------------------------------------------------------------------------
    while True:

        # Tick
        clock.tick(FPS)

        # Paint background
        main_background()

        # Application events
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                exit()

        # Main menu
        main_menu.mainloop(surface, main_background, disable_loop=test, fps_limit=FPS)

        # Flip surface
        pygame.display.flip()

        # At first loop returns
        if test:
            break


if __name__ == '__main__':
    main()