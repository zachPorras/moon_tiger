import pygame
import os



WIDTH, HEIGHT = 900, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Moon Tiger Space Boogie")

BACKGROUND = (9, 19, 83)
FPS = 60

KITTY_IMAGE = pygame.image.load(
    os.path.join('Assets', 'kitty.png'))
# KITTY_IMAGE = pygame.transform.scale(KITTY_IMAGE, (55, 40))
# KITTY_IMAGE = pygame.transform.flip(KITTY_IMAGE, flip_y=True, flip_x=True)
RED_SPACESHIP_IMAGE = pygame.image.load(
    os.path.join('Assets', 'spaceship_red.png'))



def draw_window():
    WIN.fill(BACKGROUND)
    # draw surfaces (text or images) onto screen
    WIN.blit(KITTY_IMAGE, (300, 100))
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