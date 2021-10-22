import pygame
import os



WIDTH, HEIGHT = 900, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Moon Tiger Space Boogie")

BACKGROUND = (9, 19, 83)
FPS = 60

KITTY_IMAGE = pygame.image.load(
    os.path.join('Assets', 'kitty.png'))
KITTY_IMAGE = pygame.transform.flip(
    KITTY_IMAGE, flip_y=False, flip_x=True)
RED_SHIP_IMAGE = pygame.image.load(
    os.path.join('Assets', 'spaceship_red.png'))
RED_SHIP_IMAGE = pygame.transform.rotate(pygame.transform.scale(
    RED_SHIP_IMAGE, (55, 40)), 90)



def draw_window():
    WIN.fill(BACKGROUND)
    # draw surfaces (text or images) onto screen
    WIN.blit(KITTY_IMAGE, (650, 200))
    WIN.blit(RED_SHIP_IMAGE, (200, 200))
    pygame.display.update()


def main():
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            draw_window()

    pygame.quit()

if __name__ == "__main__":
    main()