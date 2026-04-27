import pygame

pygame.init()
pygame.font.init()

# ============ #
# Constants

WHITE = "#ffffff"
BLACK = "#000000"
RED = "#ff0000"
BLUE = "#0000ff"
GREEN = "#00ff00"

WIDTH = 640
HEIGTH = 480
FPS = 75
ROWS = 100
COLS = 100
PIXEL = WIDTH // COLS
BACKGROUND = BLACK
FONT = ("Courier New", 14)

# ============ #

window = pygame.display.set_mode((WIDTH, HEIGTH))
pygame.display.set_caption("MyPaint")
clock = pygame.time.Clock()

def canvas(rows, cols, color): # the canva is a set of grids where each index is a pixel to be painted
    canvas = []

    for i in range(rows):
        canvas.append([])
        for j in range(cols):
            canvas[i].append(color)

    return canvas

def draw(window, canvas):
    window.fill(BACKGROUND)
    pygame.display.update()

# ============ #
# Pygame loop

canvas = canvas(ROWS, COLS, BACKGROUND)
is_running = True

while is_running:
    clock.tick(FPS)

    for event in pygame.event.get(): # Checks if the user closes the window and end the loop
        if event.type == pygame.QUIT:
            is_running = False

        draw(window, canvas)

pygame.quit()