import pygame
import random
from pygame.locals import *
from pathlib import Path
import time
from player import Player
from food import Food
from walls import Wall

class Game():
    def __init__(self):
        # Initialize pygame
        pygame.init()

        # Initialize game screen
        self.screen_width = 576
        self.screen_height = 1024
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        pygame.display.set_caption("Snake")
        self.screen.fill((32,32,32))
        pygame.display.flip()
        
        # Load images
        self.path = Path(__file__).parent
        snake_block = pygame.image.load(self.path/'images/snake_block.png').convert_alpha()
        food_block = pygame.image.load(self.path/'images/food_block.png').convert_alpha()
        wall_block = pygame.image.load(self.path/'images/wall_block.png').convert_alpha()

        # Initialize Variables
        SIZE = 16
        length = 2
        self.next_level = True

        # Initialize Objects
        self.snake = Player(self.screen, snake_block, SIZE, length)
        self.wall = Wall(self.screen, wall_block, SIZE)
        self.apple = Food(self.screen, food_block, SIZE)
   

    def play(self):
            # Render Objects
            self.snake.draw()
            self.snake.crawl()
            self.display_score()
            self.wall.draw()
            self.apple.draw()
            pygame.display.flip()

            # Check collisions with apple
            if self.collision_check(self.snake.x[0], self.snake.y[0], self.apple.x, self.apple.y, self.apple.size):
                self.snake.increase_length()
                self.apple.move(self.wall.x, self.wall.y)
            # Check collisions with body
            for i in range(1, self.snake.length):
               if self.collision_check(self.snake.x[0], self.snake.y[0], self.snake.x[i], self.snake.y[i], self.snake.size):
                   print("Game Over")
                   time.sleep(3)
                   exit(0)
            # Check collisions with a wall
            for i in range(self.wall.number):
                if self.collision_check(self.snake.x[0], self.snake.y[0], self.wall.x[i], self.wall.y[i], self.snake.size):
                    print("Game Over")
                    time.sleep(3)
                    exit(0)
            
            # Spawn new walls
            if (self.snake.length - 1) % 2 != 0:
                self.next_level = True
            if (self.snake.length - 1) % 2 == 0:
                if self.next_level:
                    self.wall.create_walls(random.randint(3, 12))
                    self.next_level = False
    

    def collision_check(self, x1, y1, x2, y2, size):
        if x1 >= x2 and x1 < x2 + size:
            if y1 >= y2 and y1 < y2 + size:
                return True
 

    def display_score(self):
        font = pygame.font.SysFont('arial', 24)
        score = font.render(f"Score: {self.snake.length - 1}", True, (255, 255, 255))
        self.screen.blit(score, (464, 16))


    def run(self):
        # Event loop
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_q:
                        running = False
                    if event.key == K_LEFT:
                        self.snake.move_left()
                    if event.key == K_RIGHT:
                        self.snake.move_right()
                    if event.key == K_UP:
                        self.snake.move_up()
                    if event.key == K_DOWN:
                        self.snake.move_down()
                elif event.type == QUIT:
                    running = False
            
            self.play()
            time.sleep(0.05) # Game Speed