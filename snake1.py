import pygame
import sys
import time
import random

difficulty = 25

frame_size_x = 720
frame_size_y = 480

check_errors = pygame.init()

pygame.display.set_caption('Snake')
game_window = pygame.display.set_mode((frame_size_x, frame_size_y))

black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
red = pygame.Color(255, 0, 0)
green = pygame.Color(0, 255, 0)
blue = pygame.Color(0, 0, 255)

fps_controller = pygame.time.Clock()

snake_pos = [100, 50]
snake_body = [[100, 50], [90, 50], [80, 50]]

food_pos = [random.randrange(1, (frame_size_x//10) * 10),  random.randrange(1, (frame_size_x//10) * 10)]
food_spawn = True
