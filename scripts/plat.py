import pygame
import uni_vars as uv
from math import ceil
from sprite import Sprite


class Platform(Sprite):
	def __init__(self, x, y, width, height):
		super().__init__(x, y, width, height)
		self.collider = pygame.Rect(self.x, self.y, self.width, self.height)
		self.color = (0, 0, 0)

	def render(self):
		pygame.draw.rect(uv.win, self.color, self.collider)

	def collision(self, player):
		p_collider = player.collider

		# Collision handling on Y axis
		if self.collider.colliderect(p_collider):
			for i in range(ceil(abs(player.y_vel))):
				if self.collider.colliderect(p_collider):
					player.y += abs(player.y_vel) / player.y_vel * -1
			player.y_vel = -uv.gravity

		# Collision handling on X axis
		if self.collider.colliderect(p_collider):
			for i in range(ceil(abs(player.x_vel))):
				if self.collider.colliderect(p_collider):
					if player.y + player.height < self.y+5:
						player.x += (abs(player.x_vel) / player.x_vel)
					if player.y + player.height > self.y:
						player.x += (abs(player.x_vel) / player.x_vel) * -1
			# keys = pygame.key.get_pressed()
			# player.x_vel = 0
