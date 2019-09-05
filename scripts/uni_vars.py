import pygame

width, height = 1100, 700
title = "Cube Jumper"
background = (255, 255, 255)
clock = pygame.time.Clock()
running = True
FPS = 60

win = pygame.display.set_mode((width, height))
pygame.display.set_caption(title)
