import pygame
from sprite import Sprite
import uni_vars as uv


class Cube(Sprite):
	def __init__(self, x, y, width, height):
		super().__init__(x, y, width, height)
		self.color = (255, 0, 0)
		self.collider = pygame.Rect((self.x, self.y, self.width, self.height))

	def render(self):
		pygame.draw.rect(uv.win, self.color, self.collider)
