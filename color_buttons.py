import pygame

class Button:
    "Since pygame does not have any built-in buttons we need to create our buttons and check for collision"
    def __init__(self, x, y, width, height, color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color

    def draw(self, window):
        "Draws the color button"
        pygame.draw.rect(window, self.color, (self.x, self.y, self.width, self.height))

    def is_clicked(self, pos):
        "Check if the button is active"
        x, y = pos
        if not (x >= self.x and x <= self.x + self.width):
            return False
        if not (y >= self.y and x <= self.y + self.height):
            return False
        return True