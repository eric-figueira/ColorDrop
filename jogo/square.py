import random
import pygame


class Square:
    def __init__(self, x, y, w, h, colors_dict):
        self.x = x
        self.y = y
        self.width = w
        self.height = h
        self.colors = colors_dict
        self.color = self.randomize_color(self.colors, 2)
        self.rect = (self.x, self.y, self.width, self.height)

    def randomize_color(self, colors, off):
        # off will control how many colors will NOT be available
        randomIndex = random.randint(0, len(colors) - 1 - off)
        return colors[list(colors.keys())[randomIndex]]

    def set_new_color(self, colors):
        self.color = self.randomize_color(colors, 2)

    def draw(self, win):
        pygame.draw.rect(win, self.color, self.rect)
