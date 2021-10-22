import pygame
import os


WIDTH, HEIGHT = 900, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Moon Tiger Space Boogie")

BORDER = pygame.Rect(150, 0, 3, HEIGHT)
BACKGROUND = (9, 19, 83)
GREY = (213, 213, 213)
FPS = 60
VEL = 4
KITTY_WIDTH = 65
KITTY_HEIGHT = 65
EVIL_SHIP_WIDTH = 55
EVIL_SHIP_HEIGHT = 40
kitty_orientation = 'Left'


KITTY_IMAGE = pygame.image.load(
    os.path.join('Assets', 'kitty.png'))
KITTY_IMAGE = pygame.transform.flip(
    pygame.transform.scale(
        KITTY_IMAGE, (KITTY_WIDTH, KITTY_HEIGHT)), flip_y=False, flip_x=True)
EVIL_SHIP_IMAGE = pygame.image.load(
    os.path.join('Assets', 'spaceship_red.png'))
EVIL_SHIP_IMAGE = pygame.transform.rotate(
    pygame.transform.scale(
        EVIL_SHIP_IMAGE, (EVIL_SHIP_WIDTH, EVIL_SHIP_HEIGHT)), 90)


def draw_window(evil_ship, kitty):
    WIN.fill(BACKGROUND)
    pygame.draw.rect(WIN, GREY, BORDER)
    # draw surfaces (text or images) onto screen
    WIN.blit(KITTY_IMAGE, (kitty.x, kitty.y))
    WIN.blit(EVIL_SHIP_IMAGE, (evil_ship.x, evil_ship.y))
    pygame.display.update()


def kitty_movement(keys_pressed, kitty):
    if keys_pressed[pygame.K_LEFT] and kitty.x - VEL > BORDER.x + BORDER.width:
        kitty.x -= VEL
    if keys_pressed[pygame.K_RIGHT] and kitty.x + VEL + kitty.width < WIDTH:
        kitty.x += VEL
    if keys_pressed[pygame.K_UP] and kitty.y - VEL > 0:
        kitty.y -= VEL
    if keys_pressed[pygame.K_DOWN] and kitty.y + VEL + kitty.height < HEIGHT:
        kitty.y += VEL


def main():
    # rectangle (moveable object position) instantiations
    evil_ship = pygame.Rect(70, 200, EVIL_SHIP_WIDTH, EVIL_SHIP_HEIGHT)
    kitty = pygame.Rect(650, 200, KITTY_HEIGHT, KITTY_WIDTH)

    # game speed
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        
        # kitty movement
        keys_pressed = pygame.key.get_pressed()
        kitty_movement(keys_pressed, kitty)
        
        # display surfaces
        draw_window(evil_ship, kitty)

    pygame.quit()


if __name__ == "__main__":
    main()