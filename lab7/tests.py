import pygame as pg

# initialize pygame
pg.init()

# use an image you have (.bmp  .jpg  .png  .gif)
image_file = "Mint.png"

# RGB color tuple for screen background
black = (0,0,0)

# screen width and height
sw = 640
sh = 480
# create a screen
screen = pg.display.set_mode((sw, sh))
# give the screen a title
pg.display.set_caption('image follows mouse click position')

# load an image
# convert() unifies the pixel format for faster blit
image = pg.image.load(r'C:\GitRepo\Object_Oriented_Techniques\lab7\img\Mint.png').convert()
# get the rectangle the image occupies
# rec(x, y, w, h)
start_rect = image.get_rect()
image_rect = start_rect

running = True
while running:
    event = pg.event.poll()
    keyinput = pg.key.get_pressed()
    # exit on corner 'x' click or escape key press
    if keyinput[pg.K_ESCAPE]:
        raise SystemExit
    elif event.type == pg.QUIT:
        running = False
    elif event.type == pg.MOUSEBUTTONDOWN:
        image_rect = start_rect.move(event.pos)

    # this erases the old sreen with black
    screen.fill(black)
    # put the image on the screen
    screen.blit(image, image_rect)
    # update screen
    pg.display.flip()