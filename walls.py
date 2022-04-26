import pygame
import random

class Wall():
    def __init__(self, screen, image, size):
        self.screen = screen
        self.image = image
        self.size = size
        self.x = []
        self.y = []
        # Creates game borders
        for i in range(36):
            self.x.append(i*size)
            self.y.append(0)
            self.x.append(i*size)
            self.y.append(1024-size)
        for i in range(1,63):
            self.x.append(0)
            self.y.append(i*size)
            self.x.append(576-size)
            self.y.append(i*size)


    def draw(self):
        self.number = len(self.x)
        for i in range(self.number):
            self.screen.blit(self.image, (self.x[i], self.y[i]))
            

    def create_walls(self, wall_length):
        direction = random.randint(1,2)
        new_x = random.randint(0, 35) * self.size
        new_y = random.randint(0, 63) * self.size
        for i in range(wall_length):
            if direction == 1:
                self.x.append(new_x + i * self.size)
                self.y.append(new_y)
            if direction == 2:
                self.x.append(new_x)
                self.y.append(new_y + i * self.size)