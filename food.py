import pygame
import random

class Food():
    def __init__(self, screen, image, size):
        self.screen = screen
        self.image = image
        self.size = size
        # Spawns food within game borders
        self.x = random.randint(1, 34) * self.size
        self.y = random.randint(1, 62) * self.size
    

    def draw(self):
        self.screen.blit(self.image, (self.x, self.y))

    
    def move(self, wall_x, wall_y):
        self.x = random.randint(0, 35) * self.size
        self.y = random.randint(0, 63) * self.size
        # Ensuring not spawning food inside the walls
        for i in range(len(wall_x)):
                if self.x == wall_x[i] and self.y == wall_y[i]:
                    self.x = random.randint(1, 34) * self.size
                    self.y = random.randint(1, 62) * self.size