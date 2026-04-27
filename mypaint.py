import pygame
from color_buttons import Button

pygame.init()

# ============ #
# Constants

WHITE = "#ffffff"
BLACK = "#000000"
RED = "#ff0000"
BLUE = "#0000ff"
GREEN = "#00ff00"
GRAY = "#808080"
YELLOW = "#ffff00"
OLIVE = "#808000"

WIDTH = 600
HEIGHT = 700 
FPS = 1000
ROWS = 50
COLS = 50
PIXEL_SIZE = WIDTH // COLS
BACKGROUND_COLOR = BLACK
TOOLBAR_HEIGHT = HEIGHT - WIDTH
BTN_HEIGHT = HEIGHT - TOOLBAR_HEIGHT / 2 - 25

# ============ #
# Display Settings

window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("MyPaint")

# ============ #
# Functions

def get_row_col_from_pos(pos):
    "Calculates the row and column where the mouse cursor is poiting to. POSITION // PIXEL SIZE"
    x, y = pos
    row = y // PIXEL_SIZE
    col = x // PIXEL_SIZE

    if row >= ROWS:
        raise IndexError

    return row, col

def init_grid(rows, cols, color):
    "Creates and fill the screen with pixels"
    grid = []
    for i in range(rows): # fills each row with a grid
        grid.append([])
        for j in range(cols):
            grid[i].append(color) # fills each grid with respective color
    return grid

def draw_grid(window, grid):
    "Paint the pixels with a filled rect"
    for i, row in enumerate(grid):
        for j, pixel in enumerate(row):
            pygame.draw.rect(window, pixel, (j * PIXEL_SIZE, i * PIXEL_SIZE, PIXEL_SIZE, PIXEL_SIZE))

    # DEBUG LINES
    #for i in range(ROWS + 1):
        #pygame.draw.line(window, BLACK, (0, i * PIXEL_SIZE), (WIDTH, i * PIXEL_SIZE))
    #for j in range(COLS + 1):
        #pygame.draw.line(window, BLACK, (j * PIXEL_SIZE, 0), (j * PIXEL_SIZE, HEIGHT - TOOLBAR_HEIGHT))

def draw(window, grid, buttons):
    window.fill(GRAY) 
    draw_grid(window, grid)

    for button in buttons:
        button.draw(window)

    pygame.display.update() # fill the window and updates

# ============ #
# Buttons

buttons = [Button(10, BTN_HEIGHT, 25, 25, RED), 
           Button(45, BTN_HEIGHT, 25, 25, GREEN), 
           Button(80, BTN_HEIGHT, 25, 25, BLUE),
           Button(115, BTN_HEIGHT, 25, 25, WHITE),
           Button(150, BTN_HEIGHT, 25, 25, BLACK),
           Button(185, BTN_HEIGHT, 25, 25, YELLOW),
           Button(220, BTN_HEIGHT, 25, 25, OLIVE)]

# ============ #
# Pygame Loop

is_running = True
clock = pygame.time.Clock()
grid = init_grid(ROWS, COLS, BACKGROUND_COLOR)
pencil_color = WHITE

while is_running: # check for events
    clock.tick(FPS) # Limits rendering speed to match the screen FPS

    for event in pygame.event.get(): # Checks if the user closes the window and end the loop
        if event.type == pygame.QUIT:
            is_running = False

        if pygame.mouse.get_pressed()[0]: # if mouse left click then we need to paint
            pos = pygame.mouse.get_pos() # get cursor position
            try:
                row, col = get_row_col_from_pos(pos)
                grid[row][col] = pencil_color
            except IndexError:
                for button in buttons: # checks every button to find the active one
                    if not button.is_clicked(pos):
                        continue
                    pencil_color = button.color
                    break

        if event.type == pygame.KEYDOWN: # PRESS R TO CLEAR THE PAINT
            if event.key == pygame.K_r:
                grid = init_grid(ROWS, COLS, BACKGROUND_COLOR) # fills the screen to the default background
                pencil_color = WHITE # resets pencil color

    draw(window, grid, buttons)

pygame.quit()