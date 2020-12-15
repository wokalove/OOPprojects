# Import libraries
import sys

sys.path.insert(0, '../../')

import os
import pygame
import pygame_menu

from random import randrange

# -----------------------------------------------------------------------------
# Constants and global variables
# -----------------------------------------------------------------------------
ABOUT = ['Game: Śląski świat ',
         'Author: Ola Duda',
         '',  # new line
         'Email: oladuda1999@gmail.com']
DIFFICULTY = ['EASY']
FPS = 60.0
WINDOW_SIZE = (640, 480)

clock = None  # type: pygame.time.Clock
main_menu = None  # type: pygame_menu.Menu
surface = None  # type: pygame.Surface


# -----------------------------------------------------------------------------
# Methods
# -----------------------------------------------------------------------------
  

def random_color():
    return randrange(0, 255), randrange(0, 255), randrange(0, 255)


def play_function( font, test=False):
    # Define globals
    global main_menu
    global clock
    

    # Draw random color and text
    bg_color = random_color()
    f = font.render('Name', 1, (255, 255, 255))
    f_width = f.get_size()[0]
    
    game_menu = pygame_menu.Menu(
        height=WINDOW_SIZE[1] * 0.9,
        onclose=pygame_menu.events.DISABLE_CLOSE,
        title='Game Menu',
        width=WINDOW_SIZE[0] * 0.9,
    )
    game_menu.add_text_input('First name: ', default='')
    
    # Reset main menu and disable
    # You also can set another menu, like a 'pause menu', or just use the same
    # main_menu as the menu that will check all your input.
    main_menu.disable()
    main_menu.reset(1)

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

        # Pass events to main_menu
        text_input = main_menu.add_text_input('My name: ', default='')
        main_menu.update(events)
        
        

        # Continue playing
        surface.fill(bg_color)
        surface.blit(f, ((WINDOW_SIZE[0] - f_width) / 2, WINDOW_SIZE[1] / 2))
        
        pygame.display.flip()

        # If test returns
        if test:
            break


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

    #------------------------------------------
    # game menu: game_menu
    #------------------------------------------
    game_menu = pygame_menu.Menu(
        height=WINDOW_SIZE[1] * 0.9,
        onclose=pygame_menu.events.DISABLE_CLOSE,
        title='Game Menu',
        width=WINDOW_SIZE[0] * 0.9,
    )
    game_menu.add_text_input('First name: ', default='John')
    game_menu.add_button("Play new game",pygame_menu.events.EXIT)

    # -------------------------------------------------------------------------
    # Create menus: Play Menu
    # -------------------------------------------------------------------------
    play_menu = pygame_menu.Menu(
        height=WINDOW_SIZE[1] * 0.9,
        onclose=pygame_menu.events.DISABLE_CLOSE,
        title='Play Menu',
        width=WINDOW_SIZE[0] * 0.9,
    )

    submenu_theme = pygame_menu.themes.THEME_DEFAULT.copy()
    submenu_theme.widget_font_size = 15
    play_submenu = pygame_menu.Menu(
        height=WINDOW_SIZE[1] * 0.9,
        theme=submenu_theme,
        title='Submenu',
        width=WINDOW_SIZE[0] * 0.9,
    )
    for i in range(30):
        play_submenu.add_button('Back {0}'.format(i), pygame_menu.events.BACK)
    play_submenu.add_button('Return to main menu', pygame_menu.events.RESET)

    play_menu.add_button('New game', game_menu)
   
    play_menu.add_button('Read game', play_submenu)
    play_menu.add_button('Return to main menu', pygame_menu.events.BACK)

    # -------------------------------------------------------------------------
    # Create menus:About
    # -------------------------------------------------------------------------
    about_theme = pygame_menu.themes.THEME_DEFAULT.copy()
    about_theme.widget_margin = (0, 0)
    about_theme.widget_offset = (0, 0.05)

    about_menu = pygame_menu.Menu(
        height=WINDOW_SIZE[1] * 0.9,
        onclose=pygame_menu.events.DISABLE_CLOSE,
        theme=about_theme,
        title='About',
        width=WINDOW_SIZE[0] * 0.9,
    )
    for m in ABOUT:
        about_menu.add_label(m, align=pygame_menu.locals.ALIGN_LEFT, font_size=20)
    about_menu.add_label('')
    about_menu.add_button('Return to menu', pygame_menu.events.BACK)

    # -------------------------------------------------------------------------
    # Create menus: Main
    # -------------------------------------------------------------------------
    main_theme = pygame_menu.themes.THEME_DEFAULT.copy()
    main_theme.menubar_close_button = False  # Disable close button

    main_menu = pygame_menu.Menu(
        height=WINDOW_SIZE[1] * 0.9,
        onclose=pygame_menu.events.DISABLE_CLOSE,
        theme=main_theme,
        title='Main Menu',
        width=WINDOW_SIZE[0] * 0.9
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