import pygame
import os



WIDTH, HEIGHT = 900, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Moon Tiger Space Boogie")

BACKGROUND = (9, 19, 83)
FPS = 60
VEL = 4
KITTY_WIDTH = 65
KITTY_HEIGHT = 65
RED_SHIP_WIDTH = 55
RED_SHIP_HEIGHT = 40


KITTY_IMAGE = pygame.image.load(
    os.path.join('Assets', 'kitty.png'))
KITTY_IMAGE = pygame.transform.flip(
    pygame.transform.scale(
        KITTY_IMAGE, (KITTY_WIDTH, KITTY_HEIGHT)), flip_y=False, flip_x=True)
RED_SHIP_IMAGE = pygame.image.load(
    os.path.join('Assets', 'spaceship_red.png'))
RED_SHIP_IMAGE = pygame.transform.rotate(
    pygame.transform.scale(
        RED_SHIP_IMAGE, (RED_SHIP_WIDTH, RED_SHIP_HEIGHT)), 90)



def draw_window(red_ship, kitty):
    WIN.fill(BACKGROUND)
    # draw surfaces (text or images) onto screen
    WIN.blit(KITTY_IMAGE, (kitty.x, kitty.y))
    WIN.blit(RED_SHIP_IMAGE, (red_ship.x, red_ship.y))
    pygame.display.update()


def main():
    # rectangle (moveable object position) instantiations
    red_ship = pygame.Rect(200, 200, RED_SHIP_WIDTH, RED_SHIP_HEIGHT)
    kitty = pygame.Rect(650, 200, KITTY_HEIGHT, KITTY_WIDTH)

    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        
        # kitty movement
        keys_pressed = pygame.key.get_pressed()
        if keys_pressed[pygame.K_LEFT]:
            kitty.x -= VEL
        if keys_pressed[pygame.K_RIGHT]:
            kitty.x += VEL
        if keys_pressed[pygame.K_UP]:
            kitty.y -= VEL
        if keys_pressed[pygame.K_DOWN]:
            kitty.y += VEL

        draw_window(red_ship, kitty)

    pygame.quit()

if __name__ == "__main__":
    main()