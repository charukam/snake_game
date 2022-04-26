import pygame

class Player():
    def __init__(self, screen, image, size, length):
        self.screen = screen
        self.image = image
        self.length = length
        self.size = size
        self.x = [size]*length
        self.y = [size]*length
        self.direction = 'down'


    def draw(self):
        self.screen.fill((32,32,32))
        for i in range(self.length):
            self.screen.blit(self.image, (self.x[i], self.y[i]))
    

    def move_left(self):
        self.direction = 'left'
    def move_right(self):
        self.direction = 'right'
    def move_up(self):
        self.direction = 'up'
    def move_down(self):
        self.direction = 'down'


    def crawl(self):
        for i in range(self.length-1, 0, -1):
            self.x[i] = self.x[i-1]
            self.y[i] = self.y[i-1]

        if self.direction == 'left':
            self.x[0] -= self.size
        if self.direction == 'right':
            self.x[0] += self.size
        if self.direction == 'up':
            self.y[0] -= self.size
        if self.direction == 'down':
            self.y[0] += self.size

        self.draw()


    def increase_length(self):
        self.length += 1
        self.x.append(-1)
        self.y.append(-1)
