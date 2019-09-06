import math


class Sprite:
	def __init__(self, x, y, width, height):
		self.x = x
		self.y = y
		self.width = width
		self.height = height
		self.x_vel = 0
		self.y_vel = 0

	def update(self):
		self.x += self.x_vel
		self.y += self.y_vel
