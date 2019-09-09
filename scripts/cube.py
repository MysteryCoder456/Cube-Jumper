import pygame
from sprite import Sprite
import uni_vars as uv


class Cube(Sprite):
	def __init__(self, x, y, size):
		super().__init__(x, y, size, size)
		self.color = (255, 0, 0)
		self.collider = pygame.Rect(self.x, self.y, self.width, self.height)

	def move(self, x, y):
		self.x_vel += x
		self.y_vel += y

	def touching_edges(self):
		if self.x < 0 or self.x + self.width > uv.width:
			return True
		if self.y < 0 or self.y + self.width > uv.height:
			return True

	def render(self):
		pygame.draw.rect(uv.win, self.color, self.collider)

	def update(self):
		self.x_vel *= uv.friction
		self.y_vel += uv.gravity
		super().update()
		self.collider = pygame.Rect(self.x, self.y, self.width, self.height)
