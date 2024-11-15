import pygame
import random

BOARD_ROWS = 16
BOARD_COLS = 20
LINECOLOR = (0,0,0)
SQUARE_SIZE = 32
WIDTH = 640
HEIGHT = 512


def draw_grid(screen):
    # Horizontal lines
    for i in range(1, BOARD_ROWS):
        pygame.draw.line(screen,
                         LINECOLOR,
                         (0, i * SQUARE_SIZE),
                         (WIDTH, i * SQUARE_SIZE))

    # Vertical lines
    for i in range(1, BOARD_COLS):
        pygame.draw.line(screen,
                         LINECOLOR,
                         (i * SQUARE_SIZE, 0),
                         (i * SQUARE_SIZE, HEIGHT))


def main():
    try:
        pygame.init()
        # You can draw the mole with this snippet:
        # screen.blit(mole_image, mole_image.get_rect(topleft=(0,0)))
        mole_image = pygame.image.load("mole.png")
        screen = pygame.display.set_mode((WIDTH, HEIGHT))
        # HAD DRAW GIRD UP HERE BUT SINCE FILL WITH BG IS DOWN THERE THE LINES WERE COVERED BY THE BG.

        clock = pygame.time.Clock()
        running = True
        row, col = (0,0)
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    x,y = event.pos
                    mole_rect = mole_image.get_rect(topleft = (row,col))
                    if mole_rect.collidepoint(x,y):
                        row = random.randrange(0, WIDTH, SQUARE_SIZE)
                        col = random.randrange(0, HEIGHT, SQUARE_SIZE)
            screen.fill("light green")
            draw_grid(screen)
            screen.blit(mole_image, mole_image.get_rect(topleft = (row,col)))    # prints the mole at the top left
            pygame.display.flip()
            clock.tick(60)
    finally:
        pygame.quit()


if __name__ == "__main__":
    main()
